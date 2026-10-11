# Exact Hadamard-factor tensor law for interior angles of matrix masas
## Finding
Let \(m,n\ge 2\). Let \(A_1,B_1\subset \mathrm M_m(\mathbb C)\) and \(A_2,B_2\subset \mathrm M_n(\mathbb C)\) be masas. Assume
\[
\alpha(A_1,B_1)=\frac{\pi}{2}.
\]
Then, under the canonical identification \(\mathrm M_m(\mathbb C)\otimes \mathrm M_n(\mathbb C)\cong \mathrm M_{mn}(\mathbb C)\),
\[
\boxed{\;
\cos\alpha(A_1\otimes A_2,B_1\otimes B_2)
=\frac{n-1}{mn-1}\cos\alpha(A_2,B_2).
\;}
\]
Thus a maximally angled tensor factor does not by itself make the product pair maximally angled. Instead it attenuates the residual cosine by the exact codimension ratio \((n-1)/(mn-1)\). For any fixed \(A_2,B_2\), Fourier-Hadamard choices in growing dimension \(m\) force the product angle to \(\pi/2\), with exact cosine decay of order \(m^{-1}\).

## Assumptions and scope
The algebras are complex finite-dimensional full matrix algebras with the normalized trace, and \(\alpha\) is the interior angle used for intermediate subalgebras over the scalar inclusion. Every masa in \(\mathrm M_k(\mathbb C)\) is unitarily conjugate to the diagonal masa \(\Delta^{(k)}\).

Choose unitaries \(u_1,v_1\in \mathrm U(m)\) and \(u_2,v_2\in \mathrm U(n)\) such that
\[
A_1=u_1\Delta^{(m)}u_1^*,\qquad B_1=v_1\Delta^{(m)}v_1^*,
\]
\[
A_2=u_2\Delta^{(n)}u_2^*,\qquad B_2=v_2\Delta^{(n)}v_2^*.
\]
Put \(H=u_1^*v_1\) and \(W=u_2^*v_2\). By the maximal-angle characterization of Ghosh--Kumar, the hypothesis \(\alpha(A_1,B_1)=\pi/2\) is equivalent to \(H\) being a Hadamard unitary, hence \(|H_{ij}|^2=1/m\) for all entries.

## Proof
For a unitary \(Z\in\mathrm U(k)\), define
\[
Q_k(Z)=|Z|^{\circ 2}\circ Z-\frac1k Z,
\]
where \(\circ\) is entrywise multiplication. The explicit Ghosh--Kumar formula gives
\[
\cos\alpha\!\left(\Delta^{(k)},Z\Delta^{(k)}Z^*\right)
=\frac{k}{k-1}\,\|Q_k(Z)\|_{\mathrm{op}}.
\]
Because \(H\) is Hadamard,
\[
|H|^{\circ 2}\circ H=\frac1m H.
\]
Entrywise products and Kronecker products factor, so
\[
\begin{aligned}
Q_{mn}(H\otimes W)
&=(|H|^{\circ 2}\circ H)\otimes(|W|^{\circ 2}\circ W)
   -\frac1{mn}H\otimes W\\
&=\frac1m H\otimes\left(|W|^{\circ 2}\circ W-\frac1nW\right)\\
&=\frac1m H\otimes Q_n(W).
\end{aligned}
\]
Since \(H\) is unitary, the operator norm is multiplicative on the displayed Kronecker product and \(\|H\|_{\mathrm{op}}=1\). Therefore
\[
\|Q_{mn}(H\otimes W)\|_{\mathrm{op}}=\frac1m\|Q_n(W)\|_{\mathrm{op}}.
\]
Applying the angle formula in dimensions \(mn\) and \(n\) yields
\[
\begin{aligned}
\cos\alpha(A_1\otimes A_2,B_1\otimes B_2)
&=\frac{mn}{mn-1}\frac1m\|Q_n(W)\|_{\mathrm{op}}\\
&=\frac{n-1}{mn-1}\cos\alpha(A_2,B_2),
\end{aligned}
\]
which proves the claim.

The final equivalence follows because \((n-1)/(mn-1)>0\): the product cosine is zero exactly when \(\cos\alpha(A_2,B_2)=0\), equivalently when the second pair also has angle \(\pi/2\).

## Verification
The proof uses only exact identities. The two non-elementary inputs were checked in the focal full text: the general matrix-masa angle formula and the equivalence between maximal angle and a Hadamard relative unitary. The Kronecker step is exact entrywise algebra, and the norm identity \(\|H\otimes X\|_{\mathrm{op}}=\|X\|_{\mathrm{op}}\) follows from unitarity of \(H\).

Boundary checks are consistent. If the second pair is also maximally angled, both sides are zero and the product relative unitary is Hadamard. If the second pair coincides, its cosine is \(1\), and the product cosine is exactly \((n-1)/(mn-1)\), strictly between \(0\) and \(1\) for \(m,n\ge2\).

No numerical experiment or finite enumeration is used as an infinite proof.

## Relationship to prior work
Ghosh and Kumar derive the explicit formula for the interior angle between arbitrary matrix masas and prove that maximal angle is equivalent to a Hadamard relative unitary. Their paper uses Kronecker products in the basic-construction calculation, but the inspected full text does not state the tensor-product law above or the resulting dimension-dependent orthogonalization mechanism.

Gupta and Sharma prove a different tensor stability theorem: if the same unital algebra \(P\) is tensored onto both intermediate subalgebras, then
\[
\alpha(C\otimes_{\min} P,D\otimes_{\min} P)=\alpha(C,D).
\]
That common-factor stability does not cover the present two-pair tensoring \((A_1\otimes A_2,B_1\otimes B_2)\), where the two first factors are different and maximally angled. The exact attenuation factor therefore describes a complementary tensor regime.

Targeted searches under tensor-product, Kronecker, Hadamard, orthogonal-masa, and interior-angle formulations found no statement implying the displayed factor \((n-1)/(mn-1)\). Search absence alone is not used as a novelty proof; the originality assessment rests primarily on statement-level comparison with the two directly relevant full texts.

## Limitations
The result is restricted to complex finite-dimensional matrix masas and assumes that one factor pair has maximal interior angle. It does not give a closed scalar formula for tensoring two arbitrary nonmaximal pairs, and it makes no claim relating the higher-dimensional Kadison--Kastler distance to this tensor-product angle.

The originality search may miss an older equivalent formulation in subfactor or projection-angle terminology. The statement should therefore be read as an exact new consequence supported by the inspected literature, not as a claim that no equivalent observation has ever appeared.

## References
1. I. Ghosh and S. Kumar, *Kadison--Kastler Distance and Interior Angle for Masas: Connections with Entropy and Probabilistic Index*, arXiv:2609.38206v1, 2026; especially Theorems 5.18 and 5.22.
2. V. P. Gupta and D. Sharma, *Angles Between Intermediate Operator Subalgebras*, arXiv:2602.03694v1, 2026; especially Proposition 5.5.
3. V. P. Gupta and D. Sharma, *On possible values of the interior angle between intermediate subalgebras*, arXiv:2211.07291, 2022.
