# Exact weight-three counts and parity split for norm-one binary BCH codes

## Finding
For any integer \(s\ge2\), let \(q=2^s\), \(n=q^2+q+1\), and \(C_s=\mathcal C_{(2,n,3,1)}\) be the binary narrow-sense BCH code of designed distance three. Then its exact number of words of Hamming weight three is
\[
A_3(C_s)=\frac{(q^2+q+1)(2q+1-(-1)^s)}6.
\]
Every coordinate appears in exactly \(q\) weight-three supports when \(s\) is even and exactly \(q+1\) when \(s\) is odd. All these supports are minimum-weight because the code has no nonzero words of weight below three. For \(s=2,3,4,5\), the numbers are respectively \(28,219,1456,11627\). The occurrence of the parity-dependent term is forced by whether the base field contains nontrivial cube roots of unity.

## Assumptions and scope
Let \(F=\mathbb F_{q^3}\) and \(H=\{u\in F^\times:u^{q^2+q+1}=1\}\), the kernel of the norm from \(F\) to \(\mathbb F_q\). This cyclic subgroup has order \(n\). Fix a generator \(\beta\) of \(H\); the defining condition for the binary code is \(c(\beta)=0\), where \(c(X)=\sum_{j=0}^{n-1}c_jX^j\) has binary coefficients. The conjugate zero \(\beta^2\) follows automatically. A weight-three word is therefore the indicator of an unordered triple of **distinct** elements of \(H\) whose sum is zero.

The conclusion counts codewords, not cyclic orbits, and refers to coordinates indexed by the elements of \(H\); the claim is invariant under the choice of \(\beta\). In fact the count formula also holds at \(s=1\), where \(C_1\) is the length-seven Hamming code, but the literature-led theorem is stated for \(s\ge2\).

## Proof
**Step 1: the relevant cubics and their rational-root orbits.** For \(a\in\mathbb F_q\), define
\[
f_a(T)=T^3+aT^2+(a+1)T+1.\]
No member has the root \(0\) or \(1\), because \(f_a(0)=f_a(1)=1\). For \(t\in\mathbb F_q\setminus\{0,1\}\), the condition \(f_a(t)=0\) is equivalent to
\[
a=\phi(t):=\frac{t^3+t+1}{t^2+t}.\]
Let \(U(t)=1/(1+t)\). This permutation of \(\mathbb F_q\setminus\{0,1\}\) has order three; its second iterate is \(U^2(t)=(t+1)/t\). A direct substitution (or expansion of the three roots below) gives \(\phi(U(t))=\phi(t)\). Indeed, for \(a=\phi(t)\), all three elements \(t,U(t),U^2(t)\) are roots of \(f_a\). Whenever distinct, they exhaust its three roots. Conversely, since a degree-three polynomial has at most three distinct roots, different three-element \(U\)-orbits cannot map to the same parameter \(a\).

The fixed points of \(U\) satisfy \(t^2+t+1=0\), and exist exactly when \(3\mid(q-1)\), or equivalently when \(s\) is even. In this case there are exactly two fixed points, and each maps to itself under \(\phi\), giving two different parameters. The remaining orbits all have size three. Hence the number of parameters for which \(f_a\) has a rational root is
\[
R_s=\begin{cases}(q-2)/3,&s\text{ odd},\\(q+2)/3,&s\text{ even}.\end{cases}
\]
A cubic over a field is reducible if and only if it has a rational root. Thus the exact number of irreducible members is
\[
I_s=q-R_s=\begin{cases}(2q+2)/3,&s\text{ odd},\\(2q-2)/3,&s\text{ even}.\end{cases}
\]
This is a complete count; the two fixed-point cubics in the even case are cubes of linear polynomials.

**Step 2: the norm-one intersection.** Let
\[
K_s=\bigl|\{x\in H\setminus\{1\}:1+x\in H\}\bigr|.
\]
If \(x\notin\mathbb F_q\) and \(x\in H\), its minimal polynomial over \(\mathbb F_q\) has degree three. Write it \(T^3+aT^2+bT+1\): the coefficients are the trace \(a=x+x^q+x^{q^2}\), the second elementary symmetric sum \(b=xx^q+xx^{q^2}+x^qx^{q^2}\), and the norm \(1\). Since
\[
N_{F/\mathbb F_q}(1+x)=1+a+b+1=a+b,
\]
the condition \(1+x\in H\) is exactly \(b=a+1\). Thus the degree-three solutions are precisely the three conjugate roots of each irreducible \(f_a\), giving \(3I_s\) solutions.

If instead \(x\in\mathbb F_q\cap H\), the norm condition reduces to \(x^3=1\). We must exclude \(x=1\), for which \(1+x=0\). For even \(s\), the other two cube roots satisfy \(1+x=x^2\), and both lie in \(H\). For odd \(s\), there are no other cube roots. Hence
\[
K_s=3I_s+2\mathbf1_{2\mid s}=2q+1-(-1)^s.
\]

**Step 3: count supports and coordinate incidences.** Choose an element \(h\in H\) and normalize an ordered zero-sum triple by dividing by \(h\). Its remaining elements become \(x\) and \(1+x\) for one of the \(K_s\) solutions. This gives \(nK_s\) ordered triples with a distinguished first position. Every unordered triple of three distinct elements is counted exactly six times. Therefore \(A_3(C_s)=nK_s/6\), as claimed. Moreover, each fixed element \(h\) belongs to exactly \(K_s/2\) such unordered triples, because \(x\) and \(1+x\) describe the same two other coordinates. Substitution yields degree \(q\) for even \(s\) and \(q+1\) for odd \(s\).

Weight one cannot vanish at \(\beta\), and a weight-two word would give two equal powers of \(\beta\) with distinct exponents, which is impossible. Since \(K_s>0\), weight-three words exist, and they are the minimum-weight words. This completes the proof.

## Verification
The included standard-library Python program, `BCH_weight3_verify.py`, independently constructs finite fields via irreducible binary polynomials. For \(s=1,2,3,4,5\) it enumerates all \(n\)-th roots of unity, constructs every unordered triple of distinct roots with zero sum, checks the exact multiplicity and regular incidence degree, and independently enumerates the rational-root parameter set using \(\phi\) and its order-three symmetry. Its exact integer outputs are in `BCH_weight3_verify_output.txt`. The largest tested case has \(n=1057\) and \(11627\) counted triples. These tests cover finitely many fields only; the proof establishes the universal formula.

## Relationship to prior work
Chen, Xie, and Ding (2025, arXiv:2510.22259), Section 5, formulated the minimum-distance question for this binary BCH length family; their Theorem 5.2 gave an interval for the distance, not a weight-three multiplicity. Wang, He, Yi, and Zheng (2026, arXiv:2609.00532), Section III-B, Theorem 12 and Lemma 11, proved minimum distance three by exhibiting one irreducible member of this cubic family. The present count takes the existence-based norm-one argument as motivation but determines the **entire** minimum-weight layer and the corresponding coordinate incidence, using the exact orbit structure of the rational-root map. The familiar BCH single-root condition and the known distance-three statement are not claimed as new.

The related literature on general \(q\)-ary BCH codes of lengths \((q^m-1)/(q-1)\) is not automatically equivalent: those codes use \(\mathbb F_q\)-linear rather than binary subfield-defined zero conditions, and their full weight enumerators need not specialize to this exact layer. No claim is made that existing small-code catalogues cannot already contain individual numerical coefficients.

## Limitations
This result does not determine coefficients above weight three, full decoding complexity, or a classification of all cyclic-orbit types of minimum supports. A direct equivalent of the all-parameter coefficient formula may exist in unindexed historical code enumerator or finite-geometry literature; independent novelty review is outstanding. Exhaustive checks at finitely many lengths are evidence, not a substitute for the proof.

## References
1. X. Wang, J. He, B. Yi, D. Zheng, *Solutions to Three Conjectures and an Open Problem on Binary BCH Codes*, first public 2026-09-01, arXiv:2609.00532, https://arxiv.org/abs/2609.00532, Section III-B (Lemma 11, Theorem 12).
2. H. Chen, C. Xie, C. Ding, *Infinitely many families of distance-optimal binary linear codes with respect to the sphere packing bound*, first public 2025-10-25, arXiv:2510.22259, https://arxiv.org/html/2510.22259v1, Section 5 (Theorem 5.2, Conjecture 5.3).
3. S. Zhu, Z. Sun, X. Kai, *A Class of Narrow-Sense BCH Codes*, first public 2019, arXiv:1902.04372, https://arxiv.org/abs/1902.04372 (related general-length setting, not asserted to be the same binary code).
