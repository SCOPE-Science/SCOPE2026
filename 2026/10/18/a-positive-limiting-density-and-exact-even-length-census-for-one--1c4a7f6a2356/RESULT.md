# A positive limiting density and exact even-length census for one-letter-head marker automorphisms

## Finding
For an integer \(m\ge2\), consider every binary marker \(A*\omega\), where \(\omega\in\{A,B\}^m\). In the associated map of the two-sided full binary shift, the symbol under \(*\) is flipped precisely when its immediate left neighbor is \(A\) and its next \(m\) right neighbors are \(\omega\). Let \(N_m\) count the words \(\omega\) for which this map is bijective (equivalently, involutive, by Cuezva's theorem). The same count holds for head \(B\) by exchanging the letters.

Let \((L_i)_{i\ge1}\) and \((R_i)_{i\ge1}\) be independent, independent-and-identically-distributed fair binary sequences. For \(j\ge0\), put
\[
F_j=\{R_{j+2}=A,\ (L_1,\ldots,L_j)=(R_j,\ldots,R_1)\},
\qquad \rho=\Pr\Big(\bigcap_{j\ge0}F_j^c\Big).
\]
An empty equality of words always holds. Define \(q_J=\Pr(\cap_{j=0}^JF_j^c)\) for every integer \(J\ge0\). Then
\[
\boxed{N_{2J+2}=2^{2J+2}q_J-1,\quad
0\le q_J-\rho\le 2^{-J-1}.}
\]
For every \(m\ge2\), putting \(J=\lfloor(m-2)/2\rfloor\),
\[
\boxed{\left|\frac{N_m}{2^m}-\rho\right|\le 2^{-J-1}+2^{-m}.}
\]
In particular, \(N_m/2^m\to\rho>0\). The constant is computable by a finite sum involving \(2^{J+2}\) reversed-tail words; at \(J=25\),
\[
q_{25}=\frac{1298518439058409}{4503599627370496},\qquad
\boxed{0.2883289988874315<\rho\le0.2883290137885928.}
\]
Thus approximately \(28.83\%\) of the length-\(m\) tails yield involutive marker automorphisms as \(m\to\infty\). This is a proportion within this restricted marker family, not a density among all finite-radius cellular automata.

## Assumptions and scope
All words are over the two-letter alphabet \(\{A,B\}\). The domain is the full two-sided shift \(\{A,B\}^{\mathbb Z}\), with simultaneous replacements at all matching centers. Words are distinguished by their literal tails; different length-\(m\) tails define different maps because a context matching one tail but not another witnesses unequal output at its center. The result covers every integer \(m\ge2\), with no mixing or admissibility restrictions on the tails. The equivalence between bijectivity and saturation is the established single-marker criterion in Cuezva, Theorem 3.3; the counting and limiting law below are derived from that criterion, not asserted as a new bijectivity theorem.

## Proof
**1. Translate saturation into forbidden overlaps.** For a fixed head \(A\), specialize the two clauses of Cuezva's Definition 3.1 to a one-letter head. The head is unsaturated exactly when \(\omega\) is constant. For every right-tail position \(d\in\{2,\ldots,m\}\), the corresponding letter is unsaturated exactly when
\[
\omega_{d-1}=A\quad\text{and}\quad
(\omega_{d+1},\ldots,\omega_m)=(\omega_1,\ldots,\omega_{m-d}).
\]
The first right-tail position is unsaturated only when \(\omega\) is constant, so it introduces no additional condition. Thus, letting \(E_j\) for \(0\le j\le m-2\) denote
\[
E_j=\{\omega_{m-j-1}=A,\ \omega_{m-j+1}\cdots\omega_m=\omega_1\cdots\omega_j\},
\]
the admissible tails are those avoiding all \(E_j\), except that the all-\(B\) word must also be excluded. The all-\(A\) word is already excluded by \(E_0\). For each \(j\), the equality in \(E_j\) says that \(\omega\) has period \(d=m-j\), and the letter at position \(d-1\) is \(A\). There are \(2^d\) words with that period, and exactly half satisfy this letter condition, even when the displayed prefix and suffix overlap. Therefore \(\Pr(E_j)=2^{-(j+1)}\) under a uniform random tail.

**2. Exact even-length truncation.** Put \(m=2J+2\). If \(E_j\) holds with \(j>J\), its period \(d=m-j\) satisfies \(2\le d\le J+1\). Choose the smallest positive multiple \(d'\) of \(d\) that is at least \(J+2\). Then \(J+2\le d'\le J+1+d\le m\), and a word of period \(d\) also has period \(d'\). Moreover \(\omega_{d'-1}=\omega_{d-1}=A\). Thus \(E_{m-d'}\) holds, with \(0\le m-d'\le J\). All longer-overlap exclusions are therefore subsumed by the first \(J+1\). In particular, for even \(m\), avoiding \(E_0,\ldots,E_J\) is sufficient.

**3. Independent prefix and reversed suffix.** In a finite length-\(m\) word, let \(L_i=\omega_i\), \(R_i=\omega_{m-i+1}\). When \(J=\lfloor(m-2)/2\rfloor\), the first \(J\) and last \(J+2\) coordinates do not overlap; as random bits they are independent and fair. For \(j\le J\), event \(E_j\) is exactly \(F_j\). Consequently the fraction avoiding \(E_0,\ldots,E_J\) is \(q_J\). In the even case, the preceding step and the single exceptional all-\(B\) word yield \(N_{2J+2}=2^{2J+2}q_J-1\).

**4. Limit and explicit error.** For arbitrary \(m\), let \(B_m\) denote the event of no \(E_0,\ldots,E_J\), and \(C_m\) the event of no \(E_0,\ldots,E_{m-2}\). Then \(\Pr(B_m)=q_J\), while the union bound and Step 1 give
\[
0\le q_J-\Pr(C_m)\le\sum_{j=J+1}^{m-2}2^{-(j+1)}\le2^{-J-1}.
\]
Removing the all-\(B\) word changes the probability by exactly \(2^{-m}\). Independently, the infinite union bound gives \(0\le q_J-\rho\le\sum_{j=J+1}^\infty2^{-(j+1)}=2^{-J-1}\). Both \(N_m/2^m\) and \(\rho\) lie below \(q_J\); the absolute difference between two numbers below the same upper bound is at most their larger deficit, here at most \(2^{-J-1}+2^{-m}\). This proves the estimate and convergence.

**5. Explicit finite-sum evaluation.** For each \(u=(u_1,\ldots,u_{J+2})\in\{A,B\}^{J+2}\), define the active indices \(A(u)=\{j:0\le j\le J,\ u_{j+2}=A\}\). Each such \(j\) forbids the left-prefix cylinder \((L_1,\ldots,L_j)=(u_j,\ldots,u_1)\). Retain an active index \(j\) in \(I(u)\) precisely when no smaller active \(i<j\) satisfies \((u_1,\ldots,u_i)=(u_{j-i+1},\ldots,u_j)\). All the retained cylinders are pairwise disjoint: if cylinders of two different lengths intersect, the shorter is a prefix of the longer and the longer would not be retained. Hence the number of length-\(J\) left words avoiding all forbidden cylinders equals \(2^J-\sum_{j\in I(u)}2^{J-j}\). This proves the exact rational formula
\[
q_J=2^{-(2J+2)}\sum_{u\in\{A,B\}^{J+2}}
\left(2^J-\sum_{j\in I(u)}2^{J-j}\right).
\]
The summand is nonnegative and integer. Its evaluation at \(J=25\) is \(1298518439058409/2^{52}\). The claimed rigorous interval for \(\rho\) follows by subtracting \(2^{-26}\) from \(q_{25}\); its lower endpoint is strictly positive. The decimal endpoints quoted above are outward rounded.

## Verification
The accompanying `verify_marker_density.py` independently implements the literal saturation clauses and enumerates every binary word at lengths \(2\) through \(15\), verifying the even-length identity and cross-checking the prefix-cylinder count. The accompanying `marker_density_fast.cpp` implements the integer finite-sum formula for \(0\le J\le25\), using unsigned 64-bit integers for values strictly below \(2^{53}\); it prints the exact numerator of \(q_{25}\). The executable and the Python script are independent finite cross-checks, not substitutes for Steps 1–5 of the proof. For reproducibility: run `python3 verify_marker_density.py`; compile with `c++ -std=c++17 -O3 marker_density_fast.cpp -o marker_density_fast` and run `./marker_density_fast`. No external data or dependencies beyond a C++17 compiler and Python 3 are needed.

## Relationship to prior work
Cuezva (2026), Definitions 2.1 and 3.1 and Theorem 3.3, supply the marker construction and the bijective/involutive/saturated equivalence. Section 4 provides a short explicit list of small marker automorphisms, including \(A*BA\), \(A*BBA\), and \(A*ABB\), consistent with \(N_2=1\) and \(N_3=2\). Its statements do not furnish the even-length enumeration, the independent-boundary representation, or the positive limiting density. Boyle, Lind, and Rudolph (1988) study general marker constructions and automorphism groups of shifts of finite type, including very different global automorphism-count growth; their general results do not supply this restricted exact census or its limiting constant. Older overlap constructions are conceptual antecedents, not claimed as new here.

## Limitations
The theorem concerns a fixed head of length one and freely chosen binary tails, not multiple marker rules, longer heads, or arbitrary reversible cellular automata. No claim is made that every such automorphism is geometrically realizable by monodromy of a Hénon loop. The constant \(\rho\) is specified by a convergent event intersection and rational bounds, not by a closed elementary expression. Bibliographic overlap with historical overlap-avoidance word enumerations, including inaccessible complete texts, remains possible; no independent audit has been carried out.

## References
1. Ivan Cuezva, *Marker endomorphisms for complex Hénon maps*, arXiv:2609.24449v1 (first submitted 2026-09-21), especially Definitions 2.1, 3.1, Theorem 3.3, and Section 4; https://arxiv.org/html/2609.24449v1 .
2. Mike Boyle, Douglas Lind, and Daniel Rudolph, *The Automorphism Group of a Shift of Finite Type*, Transactions of the American Mathematical Society 306 (1988), 71–114, DOI: 10.1090/S0002-9947-1988-0927684-2, especially its marker-construction discussion.
3. G. A. Hedlund, *Endomorphisms and automorphisms of the shift dynamical system*, Mathematical Systems Theory 3 (1969), 320–375 (background on the full shift and permutive local rules; complete text not inspected).
