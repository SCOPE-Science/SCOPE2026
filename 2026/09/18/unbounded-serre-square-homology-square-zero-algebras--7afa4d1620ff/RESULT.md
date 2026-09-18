# Unbounded Serre-square homology for square-zero local algebras

## Result

Let \(k\) be a field, let \(r\ge 2\), and set
\[
A_r=k[x_1,\dots,x_r]/(x_i x_j:1\le i,j\le r)
      =k\oplus V,\qquad V^2=0,\quad \dim_kV=r.
\]
Write \(E=D A_r=\operatorname{Hom}_k(A_r,k)\). Then
\[
\dim_k\operatorname{Tor}^{A_r}_n(E,E)=
\begin{cases}
r(r^2-2),&n=1,\\[2mm]
(r^2-1)^2r^{\,n-2},&n\ge2.
\end{cases}
\]
In particular,
\[
H_n\!\left(D A_r\otimes^{\mathbf L}_{A_r}D A_r\right)\ne0
\qquad\text{for every }n\ge1,
\]
so the square of the Serre bimodule need not be a bounded complex for a finite-dimensional algebra.

For the smallest member \(A_2=k[x,y]/(x,y)^2\), the positive-degree dimensions are
\[
4,9,18,36,72,\ldots.
\]

## Consequence for the coefficient spectral sequence

Theorem 4.1 of Marco Armenta, *The Serre--Hochschild plane of a finite-dimensional algebra*, arXiv:2609.20220v1, begins with the assertion that for every finite-dimensional algebra and \(m\ge2\),
\[
W=(D A)^{\otimes_A^{\mathbf L}m}
\]
is bounded, with \(H_q(W)=0\) for \(q\gg0\), and its proof filters \(W\) by a finite Postnikov tower. The family above disproves that boundedness assertion already for \(m=2\). Thus the finite-row construction and automatic convergence argument given there do not apply to arbitrary finite-dimensional algebras as stated.

This does not affect the later Gorenstein finite-amplitude clause of that theorem: finite one-sided projective dimension of \(D A\) supplies the missing Tor-amplitude hypothesis. More generally, a finite-row version is valid under a finite Tor-amplitude assumption on the relevant Serre tensor powers. Without such an assumption, one needs an unbounded hypercohomology spectral sequence together with separate convergence hypotheses.

No claim is made here that the definition of the Serre--Hochschild plane itself fails, or that every conclusion of arXiv:2609.20220v1 depends on the finite-row assertion.

## Proof

Let \(1,x_1,\dots,x_r\) be the standard basis of \(A_r\), and let
\(f_0,f_1,\dots,f_r\) be its dual basis in \(E=D A_r\). Since \(A_r\) is commutative,
\[
x_i f_j=\delta_{ij}f_0,\qquad x_if_0=0.
\]
Hence \(E/\operatorname{rad}A_r\,E\) has basis
\(\bar f_1,\dots,\bar f_r\), so a projective cover is
\[
\pi:P_0=A_r^r\longrightarrow E,\qquad e_j\longmapsto f_j.
\]

Write an element of \(\operatorname{rad}P_0\) as
\(\sum_{i,j}c_{ij}x_i e_j\). Its image under \(\pi\) is
\((\sum_i c_{ii})f_0\). Therefore
\[
\Omega E=\ker\pi
\]
is the trace-zero hyperplane in \(\operatorname{rad}P_0\), so
\[
\Omega E\cong k^{\,r^2-1}
\]
and is annihilated by \(\operatorname{rad}A_r\).

For any semisimple module \(k^s\), its projective cover \(A_r^s\to k^s\) has kernel
\((\operatorname{rad}A_r)^s\cong k^{rs}\). It follows inductively that a minimal projective resolution \(P_\bullet\to E\) has
\[
P_0=A_r^r,\qquad
P_n=A_r^{\beta_n}\quad(n\ge1),\qquad
\beta_n=(r^2-1)r^{n-1}.
\]
For \(n\ge2\), bases may be chosen so that \(d_n:P_n\to P_{n-1}\) is a direct sum of projective covers of simples: on each target copy it has the form
\[
A_r^r\longrightarrow A_r,\qquad
(a_1,\dots,a_r)\longmapsto\sum_i a_i x_i.
\]

Tensor this resolution with \(E\). Since each \(x_i\) sends \(f_i\) to \(f_0\) and kills the other basis vectors, the induced map
\[
d_n\otimes E:E^{\beta_n}\longrightarrow E^{\beta_{n-1}}
\]
has rank \(\beta_{n-1}\) for every \(n\ge2\). For \(d_1\otimes E\), the image lies in the \(r\)-dimensional socle of \(E^r\), and the off-diagonal relations \(x_i e_j\) with \(i\ne j\) show that all \(r\) socle coordinates occur; hence
\[
\operatorname{rank}(d_1\otimes E)=r.
\]

Thus, for \(n=1\),
\[
\begin{aligned}
\dim\operatorname{Tor}_1^{A_r}(E,E)
&=(r+1)\beta_1-\operatorname{rank}(d_1\otimes E)
-\operatorname{rank}(d_2\otimes E)\\
&=(r+1)(r^2-1)-r-(r^2-1)
=r(r^2-2).
\end{aligned}
\]
For \(n\ge2\),
\[
\begin{aligned}
\dim\operatorname{Tor}_n^{A_r}(E,E)
&=(r+1)\beta_n-\beta_{n-1}-\beta_n\\
&=r\beta_n-\beta_{n-1}\\
&=(r^2-1)^2r^{n-2}.
\end{aligned}
\]
All these dimensions are positive for \(r\ge2\), proving the claim.

## Relation to prior work and limitations

Armenta's earlier paper *\(\tau\)-Hochschild (co)homology, the square of the Serre bimodule, and the Coxeter automorphism of the Tamarkin--Tsygan calculus* (arXiv:2607.10913) already identifies
\(\operatorname{Tor}^{A}_n(D A,D A)\) as the derived part of the square of the Serre bimodule. That identification is prior work. Likewise, infinite minimal resolutions over radical-square-zero local rings are classical.

The contribution here is the explicit all-degree calculation above and its use to isolate a missing hypothesis in the finite-row assertion and proof of Theorem 4.1 of arXiv:2609.20220v1. Targeted searches for the paper identifier, theorem number, the boundedness assertion, and the square-zero example found no existing correction or equivalent counterexample. Originality is therefore claimed only to the best of our knowledge. The exact Tor formula may be recoverable from older local-homological calculations under different notation; such prior occurrence would not change the counterexample to the stated boundedness claim.

## References

1. Marco Armenta, *The Serre--Hochschild plane of a finite-dimensional algebra*, arXiv:2609.20220v1. https://arxiv.org/abs/2609.20220
2. Marco Armenta, *\(\tau\)-Hochschild (co)homology, the square of the Serre bimodule, and the Coxeter automorphism of the Tamarkin--Tsygan calculus*, arXiv:2607.10913. https://arxiv.org/abs/2607.10913
