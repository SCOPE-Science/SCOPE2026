# The sharp full-support threshold for binary three-factor spectra

## Finding
For every integer \(n\ge 14\), the **unique** most populous length-\(n\) fiber of the binary, multiplicity-free, contiguous three-factor spectrum is the fiber with all eight binary triples present. At length \(n=13\), the maximizing spectra are instead the two distinct sets missing just \(000\) or just \(111\); each has \(989\) preimages, compared with \(934\) for the full spectrum. At length \(14\), the full-spectrum fiber has \(2632\) members and the largest other fiber has \(2218\).

More precisely, put \(B=\{0,1\}^3\), \(F_3(w)=\{w_iw_{i+1}w_{i+2}:1\le i\le n-2\}\) for \(w\in\{0,1\}^n\), and \(c_n(S)=|\{w:F_3(w)=S\}|\) for \(S\subseteq B\). Then
\[
\forall n\ge14,\qquad c_n(B)>\max_{S\subsetneq B}c_n(S).
\]
The resulting exact maximum \(A_n=c_n(B)\), for every \(n\ge14\), admits the explicit 256-term inclusion-exclusion formula
\[
A_n=\sum_{T\subseteq B}(-1)^{|T|}\,\mathbf{1}^{\mathsf T}M_T^{\,n-2}\mathbf{1},
\]
where \(\mathbf 1=(1,1,1,1)^{\mathsf T}\) and \(M_T\) is the \(4\times4\) matrix described below. Thus the all-positive output of eight binary three-mer membership tests becomes the unique worst-case reconstruction-ambiguity profile exactly from length \(14\) onward.

## Assumptions and scope
Words are **linear** (not cyclic), indexed from \(1\) to \(n\), and have exactly known length \(n\). Every contiguous triple is observed only as **present or absent**, ignoring occurrence counts and positions. No noisy probes, length mixtures, endpoint labels, or nonbinary alphabets are allowed. Distinct labeled binary words are counted separately, including reversals and complements.

For a state \(s\in\{0,1,2,3\}\), interpret \(s\) as the last two bits of a word, and let appending \(b\in\{0,1\}\) produce the triple indexed by \(e=2s+b\). The next state is \(t=e\bmod 4\). For a forbidden set \(T\subseteq B\), let \((M_T)_{s,t}=1\) exactly when this transition exists and its triple is not in \(T\), and \(0\) otherwise. This definition determines \(M_T\) without any multiplicities: each allowed \((s,t)\) has a unique appended bit.

## Proof
**Step 1: complete finite recurrence.** Identify each triple with its integer index \(e\in\{0,\ldots,7\}\); a bit mask \(m\in\{0,\ldots,255\}\) records precisely which triples appeared. Let \(P_j(s,m)\) count length-\(j\) words with last-two-bit state \(s\) and mask \(m\). Initially \(P_2(s,0)=1\) for all four states and all other entries are zero. Every length-\((j+1)\) word is formed from its unique length-\(j\) prefix by appending exactly one bit. Hence the exact transition, for both \(b=0,1\), is
\[
P_{j+1}( (2s+b)\bmod 4,\ m\mathbin{\mathrm{OR}}2^{2s+b})
\mathrel{+}=P_j(s,m).
\]
There are no missing or duplicate words in this recurrence. It follows that \(c_j(S)=\sum_{s=0}^3 P_j(s,m_S)\), where \(m_S\) is the mask of \(S\). A fully specified exact-integer implementation, `verify_presence_dp.py`, enumerates all \(256\) masks at **every** length \(3\le j\le50\). The complete reproducible table is `finite_profiles_3_to_50.csv`. It proves the strict inequality \(c_j(B)>\max_{S\ne B}c_j(S)\) separately for every \(14\le j\le50\). For \(j=13\), the exact maximizing masks are `0x7f` and `0xfe`, each with \(989\) words, while `0xff` has \(934\). At \(j=14\), `0xff` has \(2632\) and the best non-full mask has \(2218\). This is a **finite exhaustive computation**, with explicit state space and exact transition; it is not used to infer the infinite tail.

**Step 2: uniform infinite-tail bound.** Under the uniform distribution on the \(2^n\) words, fix any one triple \(e\in B\) and split the first \(3\lfloor n/3\rfloor\) bits into \(t=\lfloor n/3\rfloor\) disjoint three-bit blocks. The \(t\) block values are independent, and each avoids \(e\) with probability \(7/8\). Any word avoiding \(e\) in *every* contiguous window avoids it in particular in these disjoint windows. Consequently
\[
|\{w:e\notin F_3(w)\}|\le 2^n(7/8)^t.
\]
If \(S\subsetneq B\), select any \(e\in B\setminus S\); then \(c_n(S)\le 2^n(7/8)^t\). Conversely, the union bound over the eight missing-triple events yields \(c_n(B)\ge 2^n(1-8(7/8)^t)\). Since
\[
9(7/8)^{17}=\frac{2093674625884863}{2251799813685248}<1,
\]
for all \(n\ge51\) we have \(t\ge17\), and thus \(c_n(B)>2^n(7/8)^t\ge c_n(S)\) for every proper \(S\). Together with Step 1 this proves the theorem for **every** \(n\ge14\), and the counterexample at \(13\) proves sharpness of the threshold.

**Step 3: exact formula.** The number of length-\(n\) words avoiding every triple in a specified set \(T\) equals \(\mathbf1^{\mathsf T}M_T^{\,n-2}\mathbf1\): choose one of the four two-bit initial states, then make \(n-2\) allowed transitions. Inclusion-exclusion over the eight mandatory triple occurrences gives the displayed formula for \(c_n(B)\). It is an all-length exact expression, not a finite sample extrapolation.

## Verification
Run in a directory containing all packaged files:

```
python3 verify_presence_dp.py
python3 verify_presence_raw.py
python3 verify_presence_ie.py
```

The first program exhausts the complete \(4\times256\) recurrence to length \(50\), checks each population sum equals \(2^n\), and checks uniqueness for all \(14\le n\le50\). The second independently enumerates **all** \(2^n\) binary words for each \(3\le n\le18\), reconstructing their support masks directly from the word bits. The third independently evaluates the \(256\) inclusion-exclusion forbidden-transition systems for thirteen specified lengths from \(13\) through \(25\). All integer arithmetic is exact. The finite CSV table contains the full-spectrum and runner-up populations and every maximizing mask for lengths \(3\) to \(50\). The proof for \(n\ge51\) is the rational inequality in Step 2, not a program output.

## Relationship to prior work
Presence-only fixed-length substring spectra arise in sequencing by hybridization and existential pattern queries [1,2]. The same set-valued \(k\)-spectrum and its de Bruijn-walk interpretation are explicitly formalized by Bernardini and collaborators [6], who study **shortest** equivalent strings, output-sensitive listing, and privacy applications, not the global maximum fiber size among **exactly length-\(n\)** binary words. Their Section 2 and final remarks discuss the lack of a general counting analogue of the BEST theorem; the present specialized result gives a sharp modal spectrum and exact count for fixed \(k=3\) without claiming a general counting algorithm. Karhumäki and collaborators [4] consider \(k\)-abelian equivalence, which retains the **multiplicity** of every short factor, unlike presence-only equivalence. Marcovich and Yaakobi [5] likewise study reconstruction from a multiset of length-\(L\) substrings. Acharya and collaborators [3] study the multiset of **compositions** of substrings across all lengths. These statements do not imply the fixed-length, presence-only modal threshold. The original query-complexity work [1] and the hybridization reconstruction work [2] are directly relevant models but do not establish the precise modal comparison in their accessible summaries; see the limitations.

## Limitations
The numerical finite threshold was established with a transparent exhaustive finite-state recurrence; there is no shorter noncomputational proof here for the range \(14\) through \(50\). The infinite extension beyond that range is fully symbolic. This result does not classify all equivalence classes, optimize other factor lengths, infer reconstruction accuracy under a nonuniform source, or apply to noisy hybridization. Relevant early full texts, particularly Skiena–Sundaram (1995) and the 1975 adjacency-pattern literature, were not fully available for comparison, leaving a residual risk of earlier special-case statements.

## References
[1] S. Skiena and G. Sundaram, *Reconstructing Strings from Substrings*, Journal of Computational Biology 2 (1995), 333–353, DOI: 10.1089/cmb.1995.2.333.

[2] I. Pe'er, N. Arbili and R. Shamir, *A computational method for resequencing long DNA targets by universal oligonucleotide arrays*, PNAS 99 (2002), 15492–15496, DOI: 10.1073/pnas.232278299.

[3] J. Acharya, H. Das, O. Milenkovic, A. Orlitsky and S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439, first version 2014-03-10.

[4] J. Karhumäki, S. Puzynina, M. Rao and M. A. Whiteland, *On cardinalities of k-abelian equivalence classes*, arXiv:1605.03319, first version 2016-05-11.

[5] S. Marcovich and E. Yaakobi, *Reconstruction of Strings from their Substrings Spectrum*, arXiv:1912.11108.

[6] G. Bernardini et al., *On Strings Having the Same Length-k Substrings*, Theory of Computing Systems 70 (2026), Article 21, DOI: 10.1007/s00224-025-10240-z.
