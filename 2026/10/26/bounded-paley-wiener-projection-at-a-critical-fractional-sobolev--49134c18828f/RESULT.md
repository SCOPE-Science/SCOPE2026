# Bounded Paley–Wiener projection at a critical fractional Sobolev endpoint

## Finding

Let \(a>0\), \(1<p<2\), \(m\in\mathbb N_0\), and \(s=m+1/p\). Use the critical BMO realization of \(\dot W^{s,p}(\mathbb R)\) described by Monguzzi, Peloso, and Salvatori, and define the target by their proposed quotient realization of the critical fractional Bernstein space. Then the Paley–Wiener projection \(P_s\), initially defined on its Hilbert-space domain, extends to a bounded projection on the critical quotient space. More precisely,

\[
\|P_s\|_{\dot W^{s,p}\to \dot W^{s,p}_a}=\|T_1\|_{L^p(\mathbb R)\to L^p(\mathbb R)}=:C_p<\infty,
\]

where \(T_a\) is the Fourier multiplier with symbol \(\mathbf 1_{[-a,a]}\). In particular, the norm is independent of \(a\), \(m\), and \(s\) once \(p\) is fixed.

## Assumptions and scope

The critical index is \(s-1/p=m\in\mathbb N_0\). Since \(1<p<2\), \(s-1/2=m+(1/p-1/2)\notin\mathbb N_0\) and \(\lfloor s-1/2\rfloor=m\), so the Hilbert-space projection in the cited construction is defined with the same Taylor-polynomial order as the target normalization. The domain is the critical realization whose \(m\)-th derivative is in \(\mathrm{BMO}\), with the normalizations specified in the cited paper. The target is the proposed quotient class of entire functions of exponential type at most \(a\), with norm given by the homogeneous Sobolev seminorm.

The conclusion is conditional on that quotient-space definition. It does not prove that this critical target equals an interpolation-theoretic endpoint space.

## Proof

Write \(\Delta^{s/2}\) for the fractional Laplacian, interpreted on the homogeneous Sobolev quotient so that polynomials in its null space do not affect the class. On the Hilbert domain, \(\Delta^{s/2}\) is an isometry into \(L^2(\mathbb R)\), and the image of the Paley–Wiener subspace consists of those derivative data whose Fourier transforms are supported in \([-a,a]\). Therefore the orthogonal projection is conjugate to interval Fourier projection:

\[
\Delta^{s/2}P_s f=T_a\Delta^{s/2}f.
\]

For \(1<p<\infty\), the multiplier \(\mathbf 1_{[-a,a]}\) is bounded on \(L^p(\mathbb R)\): it is the difference of two modulated half-line Fourier projections, each bounded by the Hilbert-transform theorem. Hence

\[
\|T_a g\|_p\le \|T_a\|_{p\to p}\|g\|_p.
\]

Dilation conjugacy gives \(\|T_a\|_{p\to p}=\|T_1\|_{p\to p}=C_p\) for every \(a>0\). On the homogeneous quotient define

\[
\mathcal P_{a,s,p}[f]=[\Delta^{-s/2}T_a\Delta^{s/2}f].
\]

The inverse is taken modulo the permitted polynomials. Since \(T_a\) is a projection and its output has Fourier support in \([-a,a]\), this map is a projection onto the critical bandlimited quotient. Its norm is at most \(C_p\); because \(\Delta^{s/2}\) identifies the domain isometrically with \(L^p\), its operator norm is exactly \(C_p\). On the common Hilbert domain it agrees, as a quotient class, with \(P_s\). Transporting the map through the critical BMO normalization proves the stated extension.

## Verification

The exponent relation gives \(\lfloor s-1/2\rfloor=m\) because \(0<1/p-1/2<1/2\). The multiplier identity, boundedness, idempotence, and dilation invariance are exact; no numerical experiment is used. The proof gives an exact norm identity in terms of the standard interval Fourier-projection norm, not a closed-form numerical value for \(C_p\).

## Relationship to prior work

Monguzzi, Peloso, and Salvatori prove the noncritical projection theorem when \(s-1/p\notin\mathbb N_0\), and explicitly list critical-index projection boundedness as an open question. Their final section proposes the quotient realization used here. The present statement treats only \(1<p<2\) and the critical indices \(s=m+1/p\), and uses the interval-multiplier conjugacy to obtain the exact operator-norm reduction. Bellavita and Peloso study BMO duality and projections for ordinary Bernstein spaces; their results do not address this fractional critical Sobolev projection.

## Limitations

The result is for \(1<p<2\) only. It does not settle \(p>2\), the Hilbert critical case \(p=2\), the construction of a critical realization with all desired interpolation properties, or the identification of the proposed quotient target with the interpolation space. The originality assessment is literature-based and not an independent priority audit.

## References

1. A. Monguzzi, M. M. Peloso, and M. Salvatori, “Fractional Paley–Wiener and Bernstein spaces,” *Collectanea Mathematica* 72 (2021), 615–643. First public version: arXiv:2002.12015, 2020-02-27. DOI: https://doi.org/10.1007/s13348-020-00303-4; preprint: https://arxiv.org/abs/2002.12015.
2. C. Bellavita and M. M. Peloso, “Duality, BMO and Hankel operators on Bernstein spaces,” arXiv:2308.01818, first public 2023-08-03; published in *Journal of Functional Analysis* 288 (2025), 110708. https://arxiv.org/abs/2308.01818.
3. E. M. Stein, *Harmonic Analysis: Real-Variable Methods, Orthogonality, and Oscillatory Integrals*, Princeton University Press, 1993 (boundedness of the Hilbert transform on \(L^p\), \(1<p<\infty\)).
