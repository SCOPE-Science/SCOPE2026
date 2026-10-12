# Projective-flat compression of simplicial Gray codes

## Finding
Let \(q\) be a prime power, \(m\ge2\), and \(A,B\subseteq[m]\). Write \(a=|A|\), \(b=|B|\), \(c=|A\cap B|\), and \(t=b+c\), and assume \(a+b<2m\). For the dual-number evaluation family defined below, the projective support of the generator columns of the Gray-image code is a punctured projective simplex: precisely the complement of one projective \((t-1)\)-flat in \(\operatorname{PG}(2m-1,q)\). This convention regards a projective \((-1)\)-flat as empty when \(t=0\).

There are exactly
\[
H=\frac{q^{2m}-2q^{a+b}+q^t}{q-1},\qquad
L=\frac{2(q^{a+b}-q^t)}{q-1}
\]
projective generator-column classes with respective coordinate multiplicities \(2(q-1)\) and \(q-1\). No other nonzero column classes occur. In particular, the length of the original Gray image is \(2(q^{2m}-q^{a+b})\).

Keep exactly one generator coordinate from each projective class and multiply its column by a scalar to put it in a fixed projective normalization. The resulting **projective core** has length, dimension and complete generalized Hamming-weight hierarchy
\[
N=\frac{q^{2m}-q^t}{q-1},\qquad k=2m,\qquad
d_r=\frac{q^{2m}-q^t-q^{2m-r}+q^{\max(0,t-r)}}{q-1}\quad(1\le r\le2m).
\]
Thus all such projective cores with the same \((q,m,t)\) are monomially equivalent; no equivalence of the corresponding uncompressed Gray images is asserted.

The original Gray-image code has dual minimum distance exactly \(2\) and
\[
A_2^\perp=(q-1)\left[H\binom{2(q-1)}2+L\binom{q-1}2\right]
\]
nonzero dual words of weight two. Repair locality means the smallest number of *other* coordinate values determining a given coordinate in every codeword. If \(q>2\), every coordinate has locality exactly \(1\). If \(q=2\), exactly \(2H\) coordinates have locality \(1\) and the remaining \(L\) have locality exactly \(2\).

## Assumptions and scope
Let \(V=\mathbb F_q^m\) with standard coordinates and \(\Delta_S=\{x\in V:\operatorname{supp}(x)\subseteq S\}\). In the ring \(R=\mathbb F_q[u]/(u^2)\), use the defining set
\[
D=(V+uV)\setminus(\Delta_A+u\Delta_B).
\]
The code over \(R\) evaluates the coordinatewise bilinear ring pairing \(\langle v,d\rangle\), \(v\in R^m\), at each \(d\in D\). Apply the \(\mathbb F_q\)-linear Gray map \(\phi(z+uw)=(w,z+w)\). In a trace-pairing formulation the change of nondegenerate basis does not change the conclusions. The parameter restrictions ensure \(D\ne\varnothing\); in particular \(0\le t\le a+b<2m\).

The generalized Hamming weight \(d_r\) is the least support size among \(r\)-dimensional subcodes of the projective core, **not** of the original longer Gray image. The counts \(H,L\), dual distance and locality pertain to the original, unreduced Gray image. The term monomial equivalence permits invertible coordinate scalings and permutations.

## Proof
**1. Two excluded subspaces.** Write message vectors as \((v_1,v_2)\in V\oplus V\) and evaluation positions as \((d_1,d_2)\in V\oplus V\). The two Gray-coordinate generator columns, as column vectors in \(V\oplus V\), are
\[
T_0(d_1,d_2)=(d_2,d_1),\qquad T_1(d_1,d_2)=(d_1+d_2,d_1).
\]
Both \(T_0,T_1\) are invertible \(\mathbb F_q\)-linear maps. For \(S=\Delta_A\times\Delta_B\), let \(U_i=T_i(S)\). Both have dimension \(s=a+b\). The defining equations are \(U_0=\{(x,y):x\in\Delta_B,y\in\Delta_A\}\) and \(U_1=\{(x,y):y\in\Delta_A,x-y\in\Delta_B\}\). Hence
\[
U_0\cap U_1=\{(x,y):x\in\Delta_B,\ y\in\Delta_A\cap\Delta_B\}=T,
\qquad \dim T=t.
\]
For each \(i\), the \(i\)-th Gray-coordinate columns run exactly once through the complement \((V\oplus V)\setminus U_i\). Zero lies in each \(U_i\), so all surviving columns are nonzero.

**2. Projective support and multiplicities.** A one-dimensional projective point \(P\) contributes \(q-1\) scalar-multiple columns from half \(i\) if \(P\not\subset U_i\), and no column otherwise. Therefore every point outside \(U_0\cup U_1\) has multiplicity \(2(q-1)\), every point in their symmetric difference has multiplicity \(q-1\), and every point in their intersection is missing. The inclusion-exclusion counts in the Finding follow by counting one-dimensional subspaces in vector spaces of dimensions \(2m,s,t\). The remaining projective support is \(\operatorname{PG}(2m-1,q)\setminus\operatorname{PG}(T)\). Since \(T\) is proper, this complement spans the entire \(2m\)-dimensional vector space: take a nonzero vector \(e\) outside \(T\), a basis of \(T\), and a basis of a complement containing \(e\); each vector of \(T\) is a difference of two vectors outside \(T\). Consequently the projective core has dimension \(2m\). Every \(t\)-space is sent to every other \(t\)-space by an ambient invertible transformation, establishing the claimed core equivalence.

**3. All support weights of the core.** Write \([h]_q=(q^h-1)/(q-1)\) for \(h\ge0\). An \(r\)-dimensional message subspace has a common-zero coordinate set consisting of the projective points of a \((2m-r)\)-dimensional annihilator \(W\) outside \(T\). Its size is
\[
[2m-r]_q-[\dim(W\cap T)]_q.
\]
The dimension inequality \(\dim(W\cap T)\ge \max(0,t-r)\) is sharp: choose as much of \(W\) as possible in a linear complement of \(T\) and add the necessary basis vectors of \(T\). Thus the maximum common-zero set has size \([2m-r]_q-[\max(0,t-r)]_q\), giving the exact hierarchy displayed above. This is an exact all-ranks argument, not an extrapolation from finite experiments.

**4. Dual weight two and locality.** For a code with nonzero generator columns, its nonzero dual codewords of weight two correspond exactly to unordered proportional-column pairs with \(q-1\) nonzero relation scalars each. The multiplicity classification proves the formula for \(A_2^\perp\). It also proves that \(H>0\): with \(s\le2m-1\), the expression \(q^{2m}-2q^s+q^t\) is strictly positive. Hence dual distance is two. A coordinate participates in a weight-two dual relation exactly when its projective column class occurs at least twice. If \(q>2\), both multiplicities are at least two, so locality is one for all coordinates. If \(q=2\), heavy columns have multiplicity two and light columns occur singly, giving \(2H\) locality-one coordinates. Every light column has locality two: its vector \(x\) is outside \(T\), and \(\dim((V\oplus V)/T)=2m-t\ge2\); choose a vector \(y\) whose nonzero coset modulo \(T\) differs from that of \(x\). Then \(y\), \(x+y\), and \(x\) are distinct vectors outside \(T\). Choosing any corresponding surviving coordinate for each yields the binary weight-three parity check \(x+y+(x+y)=0\), recovering \(x\) from two other coordinates. A locality-one relation is impossible for the singly occurring light class, completing the proof.

## Verification
Run the included standalone `verification/verify.py` using Python 3 and its standard library. It constructs the two Gray halves directly over prime fields of sizes two and three and over the four-element field; enumerates all nonzero projective classes and their multiplicities; independently checks the missing projective flat, the weight-two dual count, and all generalized Hamming weights by enumeration of every reduced-row-echelon subspace for seven explicit cases. Its final marker is `VERIFY_OK`. These finite checks support, but do not replace, the preceding arbitrary-prime-power proof. For \(q=3,m=2,A=\{1\},B=\{2\}\), the program obtains \(H=33\), \(L=6\), core length \(39\), generalized hierarchy \((26,35,38,39)\), and \(A_2^\perp=408\).

## Relationship to prior work
Yadav, Tiwari and Sarma, Theorem 3.3 in their September 2026 paper, introduced and analyzed the complement-product defining set used here, deriving Lee-weight distributions and optimality/minimality conditions. Their results are premises for identifying the family, not new claims herein. The additional statement proved here identifies its *projective-column geometry*, complete multiplicities, compressed-core hierarchy, dual weight-two multiplicity, and coordinate-locality profile. The abstract punctured-simplex weight principle is classical; novelty is claimed only for its precise realization by this family with the exact unreduced multiplicities and repair consequences. Chen and collaborators (2024) analyze related dual-number codes with factorwise defining sets, including products of a complemented factor, rather than the complement of a product considered here. No general equivalence of their full-length constructions is assumed.

## Limitations
The core hierarchy does not give the complete generalized Hamming-weight hierarchy of the original repeated-column Gray image. The full-length code may retain parameter dependence on \(A,B\) beyond \(t\). The finite checker does not constitute an exhaustive search over all fields or dimensions. Prior-literature searches can miss unindexed identifications and exact-dual-count calculations. No independent audit has been performed.

## References
1. A. Yadav, A. Tiwari, R. Sarma, *Linear Codes over \(\mathbb F_q+u\mathbb F_q\) associated with Simplicial Complexes, Their Gray Images, and Subfield Codes*, arXiv:2609.11783v1, first public 2026-09-10. https://arxiv.org/abs/2609.11783
2. B. Chen, Y. Xu, Z. Hu, N. Li, X. Zeng, *Optimal linear codes with few weights from simplicial complexes*, arXiv:2407.10074v1 (2024). https://arxiv.org/abs/2407.10074
