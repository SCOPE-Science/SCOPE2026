# A two-component radial Gaussian localization mask with a nonadjacent top-mode crossing

## Finding

In the standard Bargmann–Fock space, there is an explicit two-parameter family of disconnected radial observation sets whose **optimal Gaussian concentration eigenfunction switches directly between degrees zero and two, skipping degree one**. Let
\[
s_-=(4-\sqrt{10})/3,\qquad s_+=(4+\sqrt{10})/3.
\]
For every pair of real parameters \(s_+\le a<b\le3\), put
\[
H(t)=t(1+t/2)e^{-t}.
\]
There exists a unique \(u_*(a,b)\in(0,s_-)\) solving
\[
H(u_*)=H(a)-H(b).
\]
For every \(0\le u\le s_-\), let \(\Omega_{u,a,b}=\{z\in\mathbb C:|z|^2\in[0,u]\cup[a,b]\}\). The exact optimal concentration is
\[
\mathcal C(u,a,b)=\sup_{0\ne f\in\mathcal F^2}\frac{\pi^{-1}\int_{\Omega_{u,a,b}}|f(z)|^2e^{-|z|^2}\,dA(z)}{\|f\|_{\mathcal F^2}^2}
=\max\{\lambda_0(u;a,b),\lambda_2(u;a,b)\},
\]
where
\[
\lambda_n(u;a,b)=\frac1{n!}\left(\int_0^u e^{-t}t^n\,dt+\int_a^b e^{-t}t^n\,dt\right).
\]
If \(0\le u<u_*\), precisely the nonzero multiples of \(z^2\) maximize the quotient. If \(u=u_*\), its complete maximizing subspace is \(\operatorname{span}\{1,z^2\}\), and the top eigenvalue has multiplicity exactly two. If \(u_*<u\le s_-\), precisely the nonzero constants maximize it. Every other eigenvalue lies strictly below the maximum, including the degree-one eigenvalue. For a **single** connected radial interval \(\{z:A\le|z|^2\le B\}\) the maximizing degrees always form a singleton or a pair of adjacent integers: nonadjacent top-mode degeneracy cannot occur. Hence two radial components are minimal for this mode-skipping phenomenon.

## Assumptions and scope

Let \(\mathcal F^2=\{f\text{ entire}:\|f\|^2_{\mathcal F^2}=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)<\infty\}\). The complex Hilbert-space orthonormal basis is \(e_n(z)=z^n/\sqrt{n!}\), for integers \(n\ge0\). The observation regions are closed up to boundary sets of Gaussian measure zero; \(u=0\) means that the inner disk has zero measure. Every parameter is real with \(s_+\le a<b\le3\) and \(0\le u\le s_-\). No claim is made for arbitrary disconnected masks or other weights.

## Proof

**1. Exact diagonalization and norm.** For an entire \(f=\sum_{n\ge0}c_ne_n\), angular orthogonality and monotone convergence imply
\[
\frac1\pi\int_{\Omega_{u,a,b}}|f(z)|^2e^{-|z|^2}\,dA(z)=\sum_{n\ge0}\lambda_n(u;a,b)|c_n|^2,
\qquad \|f\|_{\mathcal F^2}^2=\sum_{n\ge0}|c_n|^2.
\]
The radial localization is therefore positive and diagonal. Since \(0\le t\le3\) throughout the mask, its eigenvalues decrease factorially for large \(n\), and the supremum is the largest eigenvalue. The maximizing subspace is the span of precisely the basis vectors at the largest eigenvalue.

**2. Excluding all modes beyond degree two.** For every integer \(n\ge2\) and \(0\le t\le3\),
\[
\frac{t^{n+1}}{(n+1)!}\le\frac{t^n}{n!}.
\]
The inequality is strict for almost every \(t\) in the outer annulus, since the latter has positive width. Hence \(\lambda_2>\lambda_3>\lambda_4>\cdots\), with all quantities positive.

**3. Excluding degree one.** The polynomial \(3t^2-8t+2\) is nonnegative on precisely the two nonnegative ranges \([0,s_-]\cup[s_+,\infty)\). Consequently, for every \(t\) in the mask,
\[
t\le\frac14+\frac34\,\frac{t^2}{2}.
\]
The integrated inequality is strict because the annulus contains a positive-measure interval on which the polynomial is positive. Thus
\[
\lambda_1<\frac14\lambda_0+\frac34\lambda_2\le\max\{\lambda_0,\lambda_2\}.
\]
Steps 2 and 3 show that no omitted degree can attain the top eigenvalue, even when \(\lambda_0=\lambda_2\).

**4. A unique degree-zero/degree-two crossing.** Direct differentiation shows
\[
H'(t)=e^{-t}(1-t^2/2),\qquad
\lambda_0-\lambda_2=H(u)-H(a)+H(b).
\]
On \([0,s_-]\), the derivative \(H'(u)>0\), so the difference increases strictly in \(u\). Since \(a\ge s_+>\sqrt2\), \(H(a)>H(b)\); therefore \(\lambda_0(0)-\lambda_2(0)<0\). To show the difference is positive at \(u=s_-\), note first that \(s_->1/4\), while \(e^{-t}>1-t\ge3/4\) on \([0,1/4]\). Thus
\[
H(s_-)\ge H(1/4)=\int_0^{1/4}e^{-t}(1-t^2/2)\,dt
>\frac34\left(\frac14-\frac1{384}\right)=\frac{95}{512}.
\]
On \([s_+,3]\), the function \(q(t)=e^{-t}(t^2/2-1)\) reaches its unique maximum at \(c=1+\sqrt3\), where \(q(c)=ce^{-c}\). The inequalities \(8/3<c<3\), together with
\[
e^{8/3}>\sum_{j=0}^{4}\frac{(8/3)^j}{j!}>12,
\]
show that \(q(t)<1/4\). Moreover \(s_+>19/8\) (because \(\sqrt{10}>25/8\)). Therefore
\[
0<H(a)-H(b)=\int_a^b q(t)\,dt<\frac{b-a}{4}<\frac{5}{32}<\frac{95}{512}<H(s_-).
\]
The intermediate value theorem and strict monotonicity supply exactly one \(u_*\in(0,s_-)\), with the three stated maximizing cases. The top eigenspace at equality is exactly two dimensional by Steps 2 and 3.

**5. Connected radial masks cannot skip a top mode.** For any single annulus with radial-squared endpoints \(0<A<B<\infty\), let \(\nu_n=\frac1{n!}\int_A^Be^{-t}t^n\,dt\). Integration of an exact derivative yields
\[
\nu_n-\nu_{n+1}=\frac{e^{-B}B^{n+1}-e^{-A}A^{n+1}}{(n+1)!}.
\]
The sign changes at most once as \(n\) increases, because \((B/A)^{n+1}\) is strictly increasing. Thus the sequence first increases and then decreases; its maximizing indices are consecutive, with at most one tie between neighbors. For \(A=0\) the right side is strictly positive, so the disk has degree zero as its unique maximizer. This proves minimality of two connected components.

## Verification

The finite algebraic inequalities and a representative crossing are reproduced by the optional standalone `check.py`, using exact rational arithmetic for the certificate bounds and high-precision numerical quadrature only for illustration. The general claim is proved above for every continuum parameter choice: numerical samples are not used to infer an infinite-dimensional assertion. For example, at \(a=5/2\) and \(b=13/5\), the crossing occurs near \(u_*=0.01772927497237\); at this crossing, \(\lambda_0=\lambda_2\approx0.02538445648310\), while \(\lambda_1\approx0.02006793190186\).

## Relationship to prior work

Radial Gaussian localization has an established Hermite/Fock diagonalization. Halvdansson's 2025 article computes spectral eigenvalue profiles for disks, annuli, and finite unions of annuli, emphasizing the unordered radial eigenvalues and their **large-dilation** decreasing rearrangement. Its Proposition 2.3 gives an asymptotic error-function profile, not this finite-scale *top-eigenspace classification*, the phase equation, or the no-skip contrast with connected masks. Zelent's October 2026 work motivates concentrated Gaussian modes by reviewing the disk sharp concentration and stability picture but does not study disconnected radial masks. The present result isolates an exact finite-scale mode transition not determined by their quoted theorems alone; it is compatible with known general diagonalization formulas and does not claim the latter as new.

## Limitations

The parameter range is sufficient rather than maximal. A single disconnected mask with a crossing is proved, but there is no classification of all two-component radial masks. The literature comparison cannot rule out equivalent special examples in earlier Daubechies-localization literature, and the 2025 article supplies the general unordered eigenvalue formula. The novelty claim is restricted to the stated uniform finite-scale classification and connectivity threshold. No independent mathematical audit has been performed.

## References

1. D. Zelent, *Stability of concentration in the Paley–Wiener space*, arXiv:2610.01299v1 (first posted 2026-10-01), especially §1.2 on Gaussian/Fock concentration. https://arxiv.org/html/2610.01299v1
2. S. Halvdansson, *Empirical plunge profiles of time-frequency localization operators*, arXiv:2502.11805v1 (first posted 2025-02-17), especially Proposition 2.3 on finite unions of annuli. https://arxiv.org/abs/2502.11805
3. L. D. Abreu and M. Doerfler, *An inverse problem for localization operators*, arXiv:1202.5841 (2012), background on Gaussian localization eigenfunctions and simply connected domains. https://arxiv.org/abs/1202.5841
