# Harmonic accumulation of Hopf envelopes in the ribosome-delay model

## Result

Perera, Pilyugin, Davis and Gedeon study a three-variable delay model for ribosome abundance control and, at the positive equilibrium, write the characteristic equation in the form

\[
p(\lambda,\tau)=\mathcal A_M(\lambda)e^{-\lambda\tau}+\mathcal B_M(\lambda)=0,
\qquad M=e^{-\mu\tau}.
\]

For a fixed dilution factor \(M\), a nonzero imaginary root \(\lambda=i\omega\) must satisfy

\[
D_M(\omega):=\left|\frac{\mathcal B_M(i\omega)}{\mathcal A_M(i\omega)}\right|=1.
\]

The source paper derives the corresponding phase branches numerically, conjectures a strict ordering of their maximal growth-rate envelopes, and reports that the number of Hopf points appears to become unbounded as \(\mu\to0\). The following statement proves the envelope ordering and gives the precise harmonic accumulation mechanism. It does not require differentiating the continuation curves.

### Theorem 1 — nested Hopf envelopes and harmonic asymptotics

Let \(J\subset (0,1]\) be a compact interval on which \(D_M(\omega)=1\) has \(r\ge1\) continuous positive-frequency branches
\[
\omega_k(M)>0,\qquad k=1,\dots,r,
\]
and suppose continuous phase lifts \(\theta_k(M)\in\mathbb R\) have been chosen so that
\[
-\frac{\mathcal B_M(i\omega_k(M))}{\mathcal A_M(i\omega_k(M))}
=e^{i\theta_k(M)}.
\]
For every integer \(n\) for which \(2\pi n-\theta_k(M)>0\) on \(J\), define
\[
\tau_{k,n}(M)=\frac{2\pi n-\theta_k(M)}{\omega_k(M)},
\qquad
\mu_{k,n}(M)=\frac{-\log M}{\tau_{k,n}(M)}
=\frac{(-\log M)\omega_k(M)}{2\pi n-\theta_k(M)}.
\]
Then:

1. For every fixed \((k,M)\),
\[
\mu_{k,n+1}(M)<\mu_{k,n}(M).
\]

2. Let
\[
H_n:=\max_{1\le k\le r,\,M\in J}\mu_{k,n}(M).
\]
Whenever \(H_{n+1}>0\),
\[
H_{n+1}<H_n.
\]
Thus the maximal Hopf envelopes are strictly nested.

3. Uniformly on the finitely many branches,
\[
\mu_{k,n}(M)
=\frac{(-\log M)\omega_k(M)}{2\pi n}+O(n^{-2}),
\]
and consequently
\[
\boxed{
H_n=\frac{C_J}{n}+O(n^{-2}),
\qquad
C_J=\frac1{2\pi}\max_{k,M\in J}(-\log M)\omega_k(M).
}
\]
In particular, whenever \(C_J>0\), the Hopf envelopes accumulate at \(\mu=0\) at the sharp harmonic scale \(1/n\).

### Theorem 2 — quantitative proliferation at fixed small growth rate

Assume in addition that the \(r\) frequency branches persist continuously on \([\bar M,1]\), with \(0<\bar M<1\). After shifting each phase lift by an integer multiple of \(2\pi\) (equivalently, reindexing its delay sequence), assume the positive-delay branches are indexed by \(n=1,2,\ldots\). Fix any \(M_0\in[\bar M,1)\), and set
\[
a_0=-\log M_0,
\qquad
\omega_*:=\min_{1\le k\le r}\omega_k(M_0)>0,
\qquad
\Theta_0:=\max_{1\le k\le r}|\theta_k(M_0)|,
\]
where \(\theta_k\) denotes the shifted phase lift used in this labeling. For every integer \(N\) satisfying
\[
2\pi N+\Theta_0<\frac{a_0\omega_*}{\mu},
\]
each labelled branch \((k,n)\), \(1\le k\le r\), \(1\le n\le N\), has at least one point \(M\in(M_0,1)\) with
\[
\mu_{k,n}(M)=\mu.
\]
Hence there are at least \(rN\) imaginary-root branch intersections counted with frequency-branch multiplicity. Since a single parameter point can carry at most one index \(n\) from each fixed frequency branch, there are at least \(N\) distinct spectral Hopf parameter values. Under the generic exclusion of simultaneous multi-frequency crossings, there are at least \(rN\) distinct values.

Consequently,
\[
\#\{\text{distinct spectral Hopf points at growth rate }\mu\}
\to\infty
\qquad(\mu\downarrow0),
\]
with a lower bound of order \(1/\mu\). For the two-frequency situation reported in the source paper, the labelled-intersection lower bound carries an additional factor of two relative to the distinct-point bound, up to the explicit constant above.

## Proof

The phase relation at a positive imaginary root is
\[
e^{-i\omega_k\tau}=e^{i\theta_k},
\]
so all positive-delay representatives are
\[
\tau_{k,n}=\frac{2\pi n-\theta_k}{\omega_k}.
\]
Using \(M=e^{-\mu\tau}\) gives the displayed formula for \(\mu_{k,n}\).

For fixed \((k,M)\), increasing \(n\) adds exactly \(2\pi\) to the positive denominator and leaves the numerator unchanged. This proves the pointwise strict inequality.

Because \(J\) is compact and the branches are continuous, each \(H_n\) is attained. Let \((k_*,M_*)\) attain \(H_{n+1}>0\). Pointwise strict nesting gives
\[
H_n\ge \mu_{k_*,n}(M_*)
>\mu_{k_*,n+1}(M_*)=H_{n+1},
\]
which proves strict envelope ordering.

The continuous phase lifts are bounded on the compact interval. Therefore
\[
\frac1{2\pi n-\theta_k(M)}
=\frac1{2\pi n}+O(n^{-2})
\]
uniformly in \(k,M\). Multiplication by the bounded continuous numerator \((-\log M)\omega_k(M)\), followed by taking a maximum over the compact branch set, yields
\[
H_n=\frac{C_J}{n}+O(n^{-2}).
\]

For Theorem 2, at \(M=M_0\),
\[
\mu_{k,n}(M_0)
=\frac{a_0\omega_k(M_0)}{2\pi n-\theta_k(M_0)}
\ge
\frac{a_0\omega_*}{2\pi n+\Theta_0}.
\]
Thus the stated inequality implies \(\mu_{k,n}(M_0)>\mu\) for every \(k\) and \(n\le N\). At the other endpoint,
\[
\lim_{M\to1^-}\mu_{k,n}(M)=0,
\]
because \(-\log M\to0\), while the continued frequency and phase branches remain bounded and the relevant denominator stays positive. Continuity therefore gives at least one solution of \(\mu_{k,n}(M)=\mu\) between \(M_0\) and 1 for every label \((k,n)\). For a fixed \(k\) and fixed \(M\), the pointwise strict ordering in \(n\) prevents two different indices from producing the same parameter point. Hence at most \(r\) labels can coalesce at one parameter point, proving the distinct-point lower bound. This completes the proof.

## Consequence for the 2026 ribosome-delay analysis

In Section 4.2 of the source paper, two positive roots \(\omega_1(M)<\omega_2(M)\) are numerically reported on a dilution window approaching \(M=1\). The paper defines joined curves \(u^n=c_2^n\cup c_1^n\), their maxima \(\mu_{\max}^n\), conjectures that these maxima decrease with \(n\), and states that the number of Hopf points appears to grow without bound as \(\mu\to0\).

Whenever those two reported roots form continuous simple branches on a compact closure of such a window, Theorem 1 proves the conjectured ordering
\[
\mu_{\max}^{n+1}<\mu_{\max}^n
\]
and strengthens it to
\[
\mu_{\max}^n=C/n+O(n^{-2}).
\]
If the branches persist to \(M=1\), Theorem 2 rigorously supplies the reported unbounded proliferation mechanism at fixed small \(\mu\), with an explicit \(1/\mu\) lower bound.

The source's stronger Conjecture 1 asserts an exact count of \(2k\) Hopf points throughout each interval \(I_k=(\mu_{\max}^{k+1},\mu_{\max}^{k})\). The envelope ordering alone does not imply that exact count: one must additionally rule out multiple horizontal intersections of a single joined curve \(u^n\). The present result therefore resolves the envelope-ordering and accumulation parts, but does not claim a proof of the full exact-count conjecture.

## Limitations

- The theorems concern spectral Hopf points, meaning nonzero imaginary characteristic roots. Upgrading every such point to a nonlinear Hopf bifurcation requires the usual simplicity, transversality, and nonlinear nondegeneracy conditions.
- The fixed-\(M\) parametrization is exactly the one used in the source's Section 4.2. If underlying biological degradation parameters are instead constrained to co-vary with \(\mu\), the characteristic coefficients acquire additional \(\mu\)-dependence and require a separate perturbation analysis.
- The quantitative fixed-\(\mu\) proliferation theorem assumes that the relevant positive-frequency branches persist continuously to \(M=1\). The source reports this behavior numerically for its displayed two-root window; this record does not promote that numerical observation to a rigorous interval certification.
- Simultaneous crossings of the two frequency branches can merge two labelled events into one double-Hopf parameter value. The distinct-point bound allows for this; the factor-of-two count requires generic nonresonance.

## Originality scope

The phase formula for delay equations and elementary compactness/asymptotic arguments are standard. The contribution claimed here is source-specific: the strict ordering of the ribosome model's Hopf-envelope maxima, the sharp \(1/n\) envelope asymptotic, and the quantitative \(1/\mu\) proliferation mechanism extracted from the characteristic representation left conjectural/numerical in the 2026 paper. To the best of our knowledge, searches by article title, DOI, authors, the stated conjecture, and synonymous Hopf-branch formulations found no later correction or paper proving these source-specific statements.

## References

1. P. C. Perera, S. S. Pilyugin, L. Davis, T. Gedeon, “Effect of transcriptional delay on ribosome abundance control,” *Journal of Mathematical Biology* **93**, 2 (2026). https://doi.org/10.1007/s00285-026-02420-3
2. Open-access full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC13263304/
