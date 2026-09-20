# Sharp quantitative structure of polynomially finite-rank operators

## Result

Let \(X\) be a complex Banach space, let \(T\in\mathcal B(X)\), and let
\[
p(z)=\sum_{n=0}^d a_n z^n,\qquad d\ge 1,
\]
be a nonconstant polynomial. Assume
\[
r:=\operatorname{rank} p(T)<\infty.
\]

Then the following hold.

1. **Sharp algebraicity bound.** \(T\) is algebraic, and its minimal polynomial \(m_T\) satisfies
   \[
   \deg m_T\le d+r.
   \]
   This bound is sharp for every \(d\ge1\) and \(r\ge0\).

2. **Defect-range-localized lifting.** There is \(F\in\mathcal B(X)\) such that
   \[
   p(T-F)=0,\qquad \operatorname{Ran}F\subseteq \operatorname{Ran}p(T),
   \qquad \operatorname{rank}F\le r.
   \]

3. **Two-sided rank-distance bounds.** If
   \[
   \delta_p(T):=\min\{\operatorname{rank}(T-S):S\in\mathcal B(X),\ p(S)=0\},
   \]
   then
   \[
   \left\lceil\frac r d\right\rceil\le \delta_p(T)\le r.
   \]
   The upper constant \(1\) is sharp even for each fixed nonconstant polynomial \(p\).
   The lower factor \(1/d\) is sharp uniformly over degree-\(d\) polynomials.

The lifting statement remains valid without finite rank whenever
\(\operatorname{Ran}p(T)\) is a complemented closed subspace: one can choose
\(F\) with \(\operatorname{Ran}F\subseteq\operatorname{Ran}p(T)\) and
\(p(T-F)=0\).

## Proof

Set
\[
M:=\operatorname{Ran}p(T).
\]
Because \(p(T)\) commutes with \(T\), \(M\) is \(T\)-invariant. Under the
finite-rank hypothesis, \(M\) is finite-dimensional with \(\dim M=r\).

### Algebraicity and the degree bound

Let \(A=T|_M\). Choose a monic polynomial \(q\) of degree at most \(r\)
annihilating \(A\); for example, take the characteristic polynomial of \(A\)
when \(r>0\), and \(q=1\) when \(r=0\). For every \(x\in X\), the vector
\(p(T)x\) lies in \(M\), so
\[
q(T)p(T)x=q(A)p(T)x=0.
\]
Hence
\[
(qp)(T)=0,
\]
and therefore \(T\) is algebraic with
\[
\deg m_T\le \deg(qp)\le d+r.
\]

For sharpness, take a nilpotent Jordan block \(N\) of size \(d+r\) and
\(p(z)=z^d\). Then
\[
\operatorname{rank}p(N)=\operatorname{rank}N^d=r,
\]
while the minimal polynomial of \(N\) is \(z^{d+r}\), of degree \(d+r\).
The case \(r=0\) is the same example with a block of size \(d\).

### Localized lifting

The finite-dimensional space \(M\) is complemented, so write
\[
X=M\oplus Y.
\]
Relative to this decomposition, invariance of \(M\) gives
\[
T=
\begin{pmatrix}
A&B\\
0&D
\end{pmatrix}.
\]
Since \(p(T)(X)\subseteq M\), the lower-right block of \(p(T)\) is zero.
For a polynomial of an upper-triangular block operator, that lower-right
block is \(p(D)\). Thus
\[
p(D)=0.
\]

Choose any root \(\lambda\) of \(p\), which exists over \(\mathbb C\), and set
\[
S=
\begin{pmatrix}
\lambda I_M&0\\
0&D
\end{pmatrix},
\qquad
F:=T-S=
\begin{pmatrix}
A-\lambda I_M&B\\
0&0
\end{pmatrix}.
\]
Then \(p(S)=0\), so \(p(T-F)=0\), and the displayed block form gives
\[
\operatorname{Ran}F\subseteq M=\operatorname{Ran}p(T).
\]
Consequently \(\operatorname{rank}F\le r\).

Exactly the same argument proves the complemented-range extension: if
\(M=\operatorname{Ran}p(T)\) is closed and complemented, the block
decomposition is bounded and the same \(S\) and \(F\) work.

### Lower rank-distance bound

Let \(S\) be any operator with \(p(S)=0\), and put \(F=T-S\). The
noncommutative telescoping identity
\[
T^n-S^n=\sum_{j=0}^{n-1}T^{n-1-j}FS^j
\]
gives, after grouping by \(j\),
\[
p(T)=p(T)-p(S)
=\sum_{j=0}^{d-1}
\left(\sum_{n=j+1}^d a_nT^{n-1-j}\right)FS^j.
\]
This is a sum of \(d\) operators, each of rank at most
\(\operatorname{rank}F\). Hence
\[
r=\operatorname{rank}p(T)\le d\,\operatorname{rank}F.
\]
Minimizing over all \(p\)-algebraic \(S\) gives
\[
\delta_p(T)\ge \left\lceil\frac r d\right\rceil.
\]
The localized lifting already proved gives \(\delta_p(T)\le r\).

### Sharpness of both rank-distance constants

For the upper bound, fix any nonconstant \(p\), choose a root \(\lambda\) of
\(p\), and choose \(\mu\) with \(p(\mu)\ne0\). On an \(r\)-dimensional space
let \(T=\mu I\). Then \(\operatorname{rank}p(T)=r\). If \(p(S)=0\) and
\(\operatorname{rank}(T-S)<r\), the map \(T-S\) has a nonzero kernel
vector \(x\). Thus \(Sx=\mu x\), so
\[
0=p(S)x=p(\mu)x,
\]
a contradiction. Hence \(\delta_p(T)=r\).

For sharpness of the lower factor, take \(p(z)=z^d\). Let \(J_d\) be the
nilpotent \(d\times d\) Jordan shift and let \(C_d\) be the cyclic shift
obtained from \(J_d\) by adding the single corner map that sends the last
basis vector back to the first. Then
\[
J_d^d=0,\qquad C_d^d=I,\qquad
\operatorname{rank}(C_d-J_d)=1.
\]
Taking \(k\) direct-sum copies gives operators \(S,T\) with
\[
p(S)=0,\qquad \operatorname{rank}(T-S)=k,\qquad
\operatorname{rank}p(T)=dk.
\]
Therefore \(\delta_p(T)=k=\operatorname{rank}p(T)/d\), by the lower bound.

## Relation to prior literature

Barnes proved that if \(p(T)\) has finite-dimensional range on a Banach
space, then some finite-rank \(J\) satisfies \(p(T-J)=0\) (Corollary 11 of
*Algebraic elements of a Banach algebra modulo an ideal*, 1985). The
localized lifting above strengthens that conclusion by forcing
\(\operatorname{Ran}J\subseteq\operatorname{Ran}p(T)\), which immediately
gives the optimal universal upper estimate
\(\operatorname{rank}J\le\operatorname{rank}p(T)\).

Álvarez studied polynomially finite-rank linear relations and established
Riesz--Schauder/Fredholm structure for them in 2014. Kramar's 2012 work
states, in the reverse perturbative direction, that finite-rank
perturbations of algebraic operators are algebraic. The quantitative
minimal-polynomial bound, the defect-range localization, and the two-sided
rank-distance estimates above were not located in the inspected sources.

## Limitations

Originality is asserted only to the best of our knowledge. Barnes (1985) is
the closest exact antecedent for the lifting statement, but its Corollary 11
does not state the range localization or a rank estimate. The full text of
Kramar (2012) was not accessible in the source inspected; only its abstract
was available. Thus an equivalent quantitative formulation in that paper or
in poorly indexed literature remains a bibliographic risk.

The lower rank-distance constant \(1/d\) is claimed sharp as a universal
degree-\(d\) constant, not for every fixed polynomial of degree \(d\).

## References

1. Bruce A. Barnes, “Algebraic elements of a Banach algebra modulo an ideal,”
   *Pacific Journal of Mathematics* **117** (1985), 219–231.
   https://doi.org/10.2140/pjm.1985.117.219
2. Teresa Álvarez, “Browder Riesz–Schauder theory for polynomially finite rank
   linear relations,” *Colloquium Mathematicum* **134** (2014), 131–142.
   https://doi.org/10.4064/cm134-1-6
3. Edvard Kramar, “Some properties of algebraic operators on locally convex
   spaces,” *Acta Scientiarum Mathematicarum* **78** (2012), 147–161.
   https://acta.bibl.u-szeged.hu/16425/
