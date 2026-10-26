# Exact state complexity for binary conjugacy languages with two marked bits

## Finding

For integers \(a,b\geq0\), let \(w=1\,0^a1\,0^b\) and let \(C(w)\) be the **set** of distinct cyclic rotations of \(w\), viewed as a finite language over \(\{0,1\}\). Put \(\ell=\min(a,b)\), \(h=\max(a,b)\), and \(d=h-\ell\). The number \(\operatorname{sc}(C(w))\) of states of a smallest **complete** deterministic finite automaton accepting \(C(w)\) is exactly

\[
\boxed{\operatorname{sc}(C(w))=(2\ell+4)h+4-\ell^2-\min\{d^2,(\ell+1)^2\}.}
\]

Equivalently, the number of nonempty right quotients of this language is \(2(h+1)+(\ell+1)(2h-\ell+1)-\min\{d^2,(\ell+1)^2\}\). In particular, the reduction caused by identifying two initially different prefixes changes regime exactly when \(h\geq2\ell+1\). This formula covers every pair of nonnegative gaps, including equal gaps and two adjacent markers.

## Assumptions and scope

The alphabet is fixed as the two symbols \(0,1\); the word contains precisely two occurrences of \(1\). A cyclic rotation is a linear word of the same total length \(n=a+b+2\); equal rotations are counted only once. Complete DFA state complexity includes the unique nonaccepting sink reached by any prefix that cannot extend to a word in \(C(w)\). The empty word is not in \(C(w)\). Two words are right-equivalent if their right-quotient languages \(u^{-1}C(w)=\{v:uv\in C(w)\}\) are equal. The result concerns deterministic, not nondeterministic, automata, with no restriction on state encoding.

## Proof

**1. Quotient decomposition.** Every accepted word has length \(n\). Therefore all *nonempty* right quotients reached by prefixes of distinct lengths are distinct: the former contains words of residual length \(n-k\) at prefix depth \(k\). All prefixes not belonging to a word in \(C(w)\) share one empty quotient (the sink). At a fixed depth, a prefix containing \(j\in\{0,1,2\}\) ones has a nonempty right quotient containing only words with \(2-j\) ones; thus the three types of nonempty quotient are mutually disjoint.

**2. No-one and two-one prefixes.** A prefix containing no ones is necessarily \(0^k\), feasible at precisely the depths \(0\leq k\leq h\). Hence these contribute \(h+1\) states. A prefix containing both ones has only a zero suffix: its right quotient is the singleton \(\{0^{n-k}\}\). It exists exactly when \(\ell+2\leq k\leq n\), since the shorter cyclic zero gap can be followed between the two marked symbols. These contribute another \(h+1\) states, one at each such depth.

**3. One-one prefix regions.** Such a prefix has the unique representation \(p_{i,j}=0^i1\,0^j\) with \(i,j\geq0\). The cyclic word has two possible oriented zero gaps, so \(p_{i,j}\) is extendible exactly when

\[
(i,j)\in U:=\bigl(([0,\ell]\times[0,h])\cup([0,h]\times[0,\ell])\bigr)\cap\mathbb Z^2.
\]

The two rectangles overlap on the integer square \([0,\ell]^2\). In particular, \(|U|=2(\ell+1)(h+1)-(\ell+1)^2=(\ell+1)(2h-\ell+1)\). At each feasible \((i,j)\), the right quotient is a subset of the following two continuations:

\[
 A_{i,j}=0^{h-j}1\,0^{\ell-i}
 \quad\text{for }i\leq\ell,\ j\leq h,
\]
\[
 B_{i,j}=0^{\ell-j}1\,0^{h-i}
 \quad\text{for }i\leq h,\ j\leq\ell.
\]

The two continuations have the same length \(n-(i+j+1)\). If \(h=\ell\), both formulas coincide where defined and the map from \((i,j)\) to the singleton right quotient is injective at each fixed depth. If \(h>\ell\), a pair in the overlap square \(0\leq i,j\leq\ell\) has exactly two distinct continuations (their leading zero-run lengths differ by \(d>0\)), while every pair outside that square has exactly one continuation.

**4. Exhaust all quotient collisions.** At fixed depth \(k=i+j+1\), two different two-continuation quotient sets cannot coincide: the smaller and larger leading zero-run lengths are \(\ell-j\) and \(h-j\), so the set recovers \(j\), and then \(i=k-j-1\). They cannot coincide with singleton quotients. Within either single-orientation region, the zero-run lengths of the unique continuation similarly recover \((i,j)\). Hence any collision must be between an A-only prefix and a B-only prefix. Write the A-only coordinates \((i,j)\), so \(0\leq i\leq\ell\) and \(\ell+1\leq j\leq h\). Equating its continuation to the B-only continuation at \((i',j')\) forces

\[
 i'=i+d,\qquad j'=j-d.
\]

These coordinates form a valid B-only pair exactly when

\[
\max\{0,\ell+1-d\}\leq i\leq\ell,
\qquad
\max\{\ell+1,d\}\leq j\leq h.
\]

Both intervals contain precisely \(s=\min\{d,\ell+1\}\) integers, so there are exactly \(s^2\) disjoint paired collisions. Different A-only pairs have different continuations, and no quotient has three prefix representatives. When \(d=0\) the relevant one-orientation regions are empty and the same count \(s^2=0\) applies.

**5. State count.** The Myhill–Nerode theorem now gives exactly one empty quotient, \(2(h+1)\) no-one and two-one quotients, and \((\ell+1)(2h-\ell+1)-s^2\) one-one quotients. Therefore

\[
\operatorname{sc}(C(w))=1+2(h+1)+(\ell+1)(2h-\ell+1)-s^2
=(2\ell+4)h+4-\ell^2-\min\{d^2,(\ell+1)^2\}.
\]

All statements were exact for arbitrary \(a,b\geq0\), completing the proof.

## Verification

`checker.py` independently constructs the set of all cyclic conjugates and the full prefix trie, then minimizes that trie bottom-up by final-status and the ordered pair of child-state identifiers. It verifies the formula on every \(0\leq a\leq b<24\) (300 parameter pairs), independently counts residual right-quotient sets on every \(0\leq a\leq b<9\) (45 pairs), and verifies invariance under exchanging the gaps for every \(0\leq a,b\leq10\). For example, the state counts for gaps \((0,0),(1,1),(2,2),(2,5),(3,5),(5,10)\) are respectively \(4,9,16,31,41,94\). Run with `python3 checker.py` (standard library only). These finite tests are corroboration; the unbounded result rests on the argument above.

## Relationship to prior work

Cyclic shift is a classical regular-language operation. Jirásková and Okhotin (publicly available in December 2007) analyzed general descriptional complexity. Jirásková and Krausová (2010) proved worst-case bounds for prefix-free input languages. Gabric, Holub and Shallit (2019) determined the **unrestricted maximum**, for a conjugacy language generated by a single word, and characterized maximizers by generalized de Bruijn properties. Their full-text Section 3 gives general upper bounds and equality criteria, not the fixed-two-marker quotient collision count derived here. The present theorem is a per-word exact count throughout a constrained composition family, not a new global maximum bound.

## Limitations

The theorem handles exactly two occurrences of the distinguished symbol; it does not classify words with three or more markers, arbitrary alphabets, or nondeterministic state complexity. It counts states in complete deterministic automata, not the number of distinct rotations. The cited 2007 article and a relevant 2013 proceedings chapter could not be fully inspected from accessible sources; an overlooked special-case result under another formulation is a residual historical-priority risk. The mathematical statement has not undergone independent external review.

## References

- G. Jirásková and A. Okhotin, *State complexity of cyclic shift*, RAIRO Theoretical Informatics and Applications **42** (2008), 335–360. DOI: 10.1051/ita:2007038 (first online 2007-12-13).
- G. Jirásková and M. Krausová, *Complexity in Prefix-Free Regular Languages*, EPTCS **31** (2010), 197–204. DOI: 10.4204/EPTCS.31.22; arXiv:1008.1662.
- J. Jirásek and G. Jirásková, *Cyclic Shift on Prefix-Free Languages*, CSR 2013, 246–257. DOI: 10.1007/978-3-642-38536-0_22.
- D. Gabric, Š. Holub and J. Shallit, *Generalized de Bruijn Words and the State Complexity of Conjugate Sets*, DCFS 2019, 137–146. DOI: 10.1007/978-3-030-23247-4_10; arXiv:1903.05442.
