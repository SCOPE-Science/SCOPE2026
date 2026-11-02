# Twelve dyadic 2-Abelian ambiguity classes in the regular paperfolding word

## Finding
Let \(f=f_1f_2\cdots\) be the regular binary paperfolding word, with \(f_n=0\) when the odd part of \(n\) is \(1\pmod 4\) and \(f_n=1\) when that odd part is \(3\pmod 4\). For every integer \(k\ge4\), put \(N=2^k\) and \(q=N/4\). Among the **distinct** length-\(N\) factors of \(f\), there are exactly twelve nonempty 2-Abelian equivalence classes, with size multiset
\[
\{q-1,q-1,\;q,q,q,q,q,\;q+1,q+1,\;2q,2q,2q,2q\}.
\]
More precisely, the classes are indexed uniquely by a first letter \(a\in\{0,1\}\), last letter \(b\in\{0,1\}\), and \(h\in\{0,1,2\}\). Put
\[
B_h(00)=q+1-h,\quad B_h(01)=B_h(10)=q,\quad B_h(11)=q-1+h.
\]
The class indexed by \((a,b,h)\) consists exactly of those factors whose occurrences of any adjacent pair \(z\in\{00,01,10,11\}\) number
\[
P_{a,b,h}(z)=B_h(z)-\mathbf 1_{z=ba}.
\]
Its cardinality is
\[
\boxed{M_{a,b,h}=\binom{2}{h}B_h(ba).}
\]
In particular all four endpoint pairs occur at each of the three distinct 2-Abelian signature levels. Thus class count alone conceals a nonuniform, exactly computable multiplicity distribution.

## Assumptions and scope
A factor is a finite contiguous substring of the one-sided infinite word. Each *distinct factor string* is counted once; the number of starting positions at which it occurs is irrelevant. Two binary words of the same length are 2-Abelian equivalent when their counts of each word of lengths one and two agree. For length at least two this is equivalent to having the same endpoints and the same four overlapping adjacent-pair counts. Throughout the theorem, \(k\) is an arbitrary integer at least four, so \(N\ge16\). Circular adjacency is used only in an auxiliary counting device; the theorem concerns ordinary **linear** factors.

## Proof
**1. A complete circular catalogue.** Define \(g(r)=0\) or \(1\) according to whether the odd part of a positive integer \(r\) is \(1\) or \(3\pmod4\). For fixed \(N=2^k\) consider all length-\(N\) blocks \(g(s+1)\cdots g(s+N)\), indexed from \(s\ge0\). In any interval of \(N\) consecutive positive indices, every residue class modulo \(N\) occurs exactly once. At residues other than \(N/2\) and \(0\), the value of \(g\) is uniquely specified by the residue modulo \(N\): the exact power of two dividing the index is at most \(2^{k-2}\), so its odd part modulo four is fixed. At the two exceptional residues \(N/2\) and \(0\), denote the bits by \(y\) and \(x\), respectively. Therefore every factor is a cyclic rotation of one of the four canonical words \(C_{xy}\), formed by taking the length-\(N\) prefix \(g(1)\cdots g(N)\) and replacing its letters at one-based positions \(N/2\) and \(N\) by \(y\) and \(x\).

For each residue class of the starting position, all four choices of \((x,y)\) actually occur: write the absolute index at the residue-zero site as \(Nm\). The value there is \(g(m)\); the other special index is \(N(m\pm1/2)\), whose bit is determined by the parity of \(m\). Within either parity class of positive integers, \(g(m)\) assumes both values (take odd numbers congruent to one or three modulo four; for even numbers use twice such odd numbers). Thus the two special bits can be prescribed independently. We have exhibited all \(4N\) labelled cyclic rotations as occurring factors, while every factor occurs among those labels.

The established factor-complexity theorem of Allouche [1, Theorem in Section 5] says that every paperfolding word has exactly \(4N\) distinct length-\(N\) factors for \(N\ge7\). Hence the \(4N\) labelled words above are pairwise distinct. This is the only external mathematical theorem used in the proof; the remaining calculations are elementary. The primary proof of that theorem uses disjoint even/odd factor families and an explicit factor-count recurrence.

**2. Cyclic pair counts.** Write \(q=N/4\). In \(C_{00}\), the exceptional entries are both zero, just as in the genuine length-\(N\) prefix. At all odd one-based positions \(r\), the values alternate between zero and one. For any even position, its odd-position neighbors on the circle have opposite symbols. Each even site thus contributes exactly one unlike-letter adjacent pair and one equal-letter adjacent pair. There are \(q\) even sites with neighbors \((0,1)\) and \(q\) with neighbors \((1,0)\), giving exactly \(q\) occurrences of each of \(01\) and \(10\).

The bit at even position \(2r\) equals \(g(r)\). Let \(T(j)\) count ones in the first \(2^j\) terms of \(g\). From the alternating odd positions and the self-similar even positions, \(T(j)=2^{j-2}+T(j-1)\) for \(j\ge2\), with \(T(1)=0\), and thus \(T(j)=2^{j-1}-1\). In particular, of the \(N/2\) even positions in \(C_{00}\), precisely \(q-1\) contain one, and \(q+1\) contain zero. Thus its circular pair counts, ordered \((00,01,10,11)\), are \((q+1,q,q,q-1)\).

The two exceptional positions are each a multiple of eight, so each has a preceding \(1\) and following \(0\), including across the circular join. Changing either exceptional bit from \(0\) to \(1\) changes exactly one adjacent \(00\) to \(11\); its \(10\) count is unchanged. It follows that the circular pair counts for \(C_{xy}\) are precisely \(B_h(z)\), where \(h=x+y\).

**3. From circular cuts to 2-Abelian classes.** A length-\(N\) factor is obtained by cutting exactly one of the \(N\) circular edges of one canonical word. If the first and last letters are \(a,b\), the deleted closing edge has ordered type \(ba\). Its linear pair counts are exactly \(B_h(z)-\mathbf1_{z=ba}\), as asserted. Conversely these endpoint letters and overlapping pair counts specify the 2-Abelian equivalence class: they give all length-two counts, and the length-one counts follow from these and either endpoint.

For fixed \((x,y)\) with sum \(h\), there are precisely \(B_h(ba)\) cut edges of type \(ba\). Since the labelled rotations are all distinct, summing over the \(\binom2h\) bit pairs gives exactly \(\binom2h B_h(ba)\) distinct factors in the indicated class. The twelve signatures are mutually different: differing endpoints already distinguish classes, while for fixed endpoints differing \(h\) changes the \(00\) count. Each is nonempty because \(q\ge4\). For \(h=1\), each of the four endpoint classes has size \(2q\); for \(h=0,2\), the eight sizes are \(q-1\) twice, \(q\) four times, and \(q+1\) twice. This proves the theorem.

## Verification
The standalone `checker.py` independently constructs the sequence by a zero-based recurrence, independently constructs the four skeletons, enumerates their cyclic rotations, and counts **overlapping** adjacent pairs. For \(k=4,5,\ldots,10\) it checks: every one of the \(4N\) canonical words is different; their set agrees with all factors encountered in a prefix of length \(65N\); the circular pair formula holds for all four skeletons; and all twelve exact class signatures and cardinalities agree. The largest checked level has \(N=1024\) and \(4096\) distinct factors. Reproduce using `python3 checker.py` with the Python standard library. These finite tests corroborate, but do not establish, the unrestricted theorem.

## Relationship to prior work
Allouche [1] proves the exact ordinary factor complexity \(4N\) for every paperfolding word at all lengths \(N\ge7\), and that theorem is used above. Allouche and Bousquet-Mélou [2] analyze canonical positions of these factors. Madill and Rampersad [3] obtain the 2-regularity of the **number** of Abelian classes of paperfolding factors and give explicit complexity recurrences, not this class-size spectrum for 2-Abelian equivalence. Parreau, Rigo, Rowland and Vandomme [4] establish general regularity methods and 2-Abelian complexity results for the period-doubling and Thue–Morse words, not for the paperfolding family treated here. The present result refines the number of 2-Abelian signatures to the number of distinct factors realizing *each* signature, including their endpoint-resolved formulas. It does not claim that the underlying factor-count or regularity results are new.

## Limitations
The exact result applies only at lengths \(2^k\) with \(k\ge4\), and only to the specified regular paperfolding word. It does not classify all non-dyadic lengths, alternative folding instructions, occurrence-weighted distributions, or higher-order Abelian equivalence. The exact factor-count theorem [1] is a cited established dependency. Historical priority for this sharper fibre-size classification is not independently certified; in particular, the accessible record of [2] was not sufficient to read and compare all its full-text details.

## References
[1] J.-P. Allouche, “The number of factors in a paperfolding sequence,” *Bulletin of the Australian Mathematical Society* 46 (1992), 23–32, DOI: 10.1017/S0004972700011655. Full primary text at https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E051B7126B0C5DC6127BAD6B6C59BEA9/S0004972700011655a.pdf/the-number-of-factors-in-a-paperfolding-sequence.pdf.

[2] J.-P. Allouche and M. Bousquet-Mélou, “Canonical positions for the factors in paperfolding sequences,” *Theoretical Computer Science* 129 (1994), 263–278, DOI: 10.1016/0304-3975(94)90028-0.

[3] B. Madill and N. Rampersad, “The abelian complexity of the paperfolding word,” arXiv:1208.2856, first version 2012-08-14; *Discrete Mathematics* 313 (2013), 831–838. Full text: https://arxiv.org/pdf/1208.2856.

[4] A. Parreau, M. Rigo, E. Rowland, and É. Vandomme, “A new approach to the 2-regularity of the ℓ-abelian complexity of 2-automatic sequences,” arXiv:1405.3532, first version 2014-05-14; *Electronic Journal of Combinatorics* 22 (2015), P1.27. Full text: https://arxiv.org/pdf/1405.3532.
