# Odd-zeta crossing velocities and local zero census for logarithmic Bergman kernels

## Finding
Let \(s>0\). On the unit disk \(\mathbb D\), form the weighted analytic Hilbert space with radial weight
\[
 w_s(z)=\frac{(-\log|z|^2)^{s-1}}{\Gamma(s)}.
\]
Let its reproducing kernel be \(K_s(z,w)=P_s(z\overline w)\), where
\[
 P_s(t)=\sum_{n=0}^\infty(n+1)^s t^n
      =\frac{\operatorname{Li}_{-s}(t)}t,
 \qquad |t|<1,
\]
and \(P_s(0)=1\). For **every** integer \(m\ge1\), there exists \(\varepsilon_m>0\) such that the exact number of zeros of \(P_s\) in \(|t|<1\), with multiplicity, is
\[
 N_m(s)=\begin{cases}m-1,&2m-\varepsilon_m<s\le2m,\\m,&2m<s<2m+\varepsilon_m.\end{cases}
\]
**All** zeros in this range are simple and lie on the negative real axis. In particular, at each even positive integer, exactly one new scalar kernel zero passes through the boundary point \(t=-1\), while the other \(m-1\) zeros remain in the open disk.

Writing the unique boundary-crossing zero as \(t_m(s)\), its local real-analytic expansion is
\[
 t_m(s)=-1+v_m(s-2m)+O_m((s-2m)^2),\quad
 v_m=\frac{\pi^2}{2m+1}\,
 \frac{2^{2m+1}-1}{2^{2m+2}-1}\,
 \frac{\zeta(2m+1)}{\zeta(2m+2)}>0.
\]
Consequently \(v_m\sim \pi^2/[2(2m+1)]\) as \(m\to\infty\). At the first transition, \(v_1=14\zeta(3)/\pi^2\). Every scalar zero \(|t|<1\) corresponds to an actual zero \(K_s(z,w)=0\) by choosing \(z,w\in\mathbb D\) with \(z\overline w=t\).

## Assumptions and scope
The norm uses normalized planar area: \(\|f\|_s^2=\pi^{-1}\int_{\mathbb D}|f(z)|^2w_s(z)\,dA(z)\). The weight can be singular or vanish at the origin depending on \(s\), but is locally integrable for every \(s>0\). The parameter neighborhood \(\varepsilon_m\) may depend on \(m\); the theorem makes no assertion uniform in \(m\), nor does it classify zeros at parameters outside these neighborhoods. A zero means a zero of the single complex variable \(t=z\overline w\) inside the open unit disk, not a zero of each fixed section \(z\mapsto K_s(z,w)\).

## Proof
**1. Exact radial moments and kernel.** Set \(u=|z|^2\). Angular orthogonality and the substitution \(x=-\log u\) give
\[
 \|z^n\|_s^2=\frac{1}{\Gamma(s)}\int_0^1u^n(-\log u)^{s-1}\,du
 =\frac1{(n+1)^s},\qquad n\ge0.
\]
The monomials are a complete orthogonal basis: Fourier orthogonality and Tonelli identify the weighted norm of an analytic Taylor series with the sum of its monomial squared norms. Thus the reproducing-kernel coefficients are exactly \((n+1)^s\) and the displayed polylogarithm identity holds, with normal convergence for \(|t|<1\). Holomorphic dependence on \(t\) and analytic dependence on real \(s>0\) hold locally on the slit plane \(\mathbb C\setminus[1,\infty)\) by the standard polylogarithm continuation.

**2. Exhaustive zero count at an even integer.** For an integer \(n\ge1\),
\[
 P_n(t)=\frac{A_n(t)}{(1-t)^{n+1}},\quad A_1(t)=1,\quad
 A_{n+1}(t)=(1+nt)A_n(t)+t(1-t)A_n'(t).
\]
The recurrence proves inductively that \(A_n\) has degree \(n-1\) and precisely \(n-1\) simple negative roots: at the ordered negative roots of \(A_n\) the sign of \(A_{n+1}\) alternates, its value at \(0\) equals one, and its leading coefficient is positive, supplying one interlacing root in each required interval including the two exterior intervals. The Eulerian coefficients are palindromic, so \(t^{n-1}A_n(1/t)=A_n(t)\). For \(n=2m\), the odd-degree reciprocal polynomial therefore has the simple root \(-1\); its other \(2m-2\) roots pair reciprocally, with exactly \(m-1\) in \((-1,0)\) and \(m-1\) in \(( -\infty,-1)\). Thus \(P_{2m}\) has precisely \(m-1\) interior zeros, all simple; \(P_{2m}(-1)=0\) is an additional simple boundary root. The only singularity of the rational function near the closed disk is its pole at \(t=1\).

**3. Uniform exclusion of new zeros near the singular boundary point.** Write \(u=-\operatorname{Log}t\) for \(t\) in a small disk about \(1\), with \(t\ne1\) and \(|t|\le1\). Then \(\operatorname{Re}u\ge0\), \(u\to0\) as \(t\to1\), and Jonquière's standard expansion gives, uniformly for \(s\) in any small real neighborhood of \(2m\),
\[
 \operatorname{Li}_{-s}(e^{-u})
 =\Gamma(s+1)u^{-s-1}
 +\sum_{j=0}^\infty\zeta(-s-j)\frac{(-u)^j}{j!},
 \qquad 0<|u|<2\pi.
\]
The series is uniformly bounded as \(u\to0\) in that parameter neighborhood, whereas the leading term has modulus \(\Gamma(s+1)|u|^{-s-1}\to\infty\) uniformly. Hence \(P_s(t)\ne0\) throughout a fixed punctured neighborhood of \(t=1\) intersected with the closed disk, for all sufficiently close \(s\). This step is necessary: convergence only on compact subsets of the open disk cannot rule out newly arriving boundary zeros.

**4. No other zero branches.** Exclude that small neighborhood of \(1\). On the remaining compact part of the closed disk, \(P_s\) converges uniformly to \(P_{2m}\) and has a holomorphic continuation across its boundary. Surround each simple zero of \(P_{2m}\) on or inside the boundary by a sufficiently small pairwise disjoint complex disk, and likewise each remaining zero outside when needed; apply Rouché on their boundaries. The compact complement is zero-free, so for nearby real \(s\), the only zeros in the closed disk are the continuations of the \(m-1\) strictly interior roots and possibly the continuation of \(-1\). Simplicity and the real Schwarz symmetry of \(P_s\) make every continued root real analytic and real (uniqueness implies equality with its complex conjugate). The strictly interior roots remain negative and interior.

**5. Crossing velocity and positivity.** The eta-function identity for the analytic continuation is
\[
 P_s(-1)=\eta(-s),\qquad \eta(q)=(1-2^{1-q})\zeta(q).
\]
Here \(\eta(-2m)=0\). From \(tP_s'(t)=P_{s+1}(t)-P_s(t)\),
\[
 \partial_tP_{2m}(-1)=-\eta(-2m-1)\ne0,\qquad
 \partial_sP_s(-1)|_{s=2m}=-\eta'(-2m).
\]
The real-analytic implicit-function theorem therefore yields
\[
 t_m'(2m)=-\frac{\eta'(-2m)}{\eta(-2m-1)}.
\]
Use \(\eta'(-2m)=(1-2^{2m+1})\zeta'(-2m)\), \(\eta(-2m-1)=(1-2^{2m+2})\zeta(-2m-1)\), and the Riemann zeta functional equation to obtain
\[
 -\frac{\zeta'(-2m)}{\zeta(-2m-1)}
 =\frac{\pi^2}{2m+1}\frac{\zeta(2m+1)}{\zeta(2m+2)}.
\]
This gives the stated strictly positive \(v_m\). Therefore \(t_m(s)\) lies to the left of \(-1\) for \(s<2m\) and to its right for \(s>2m\), as long as \(|s-2m|\) is sufficiently small. Together with step 4 this proves the exact local count and simplicity. Since \(\zeta(x)\to1\) and the power-of-two ratio tends to \(1/2\), \(v_m\sim\pi^2/[2(2m+1)]\).

## Verification
The standalone `checker.py` tests exact Gamma radial moments at twelve shape/degree combinations, compares the eta-derivative velocity against the odd-zeta formula at six transitions to high precision, follows the boundary zero numerically on both sides, and constructs the Eulerian polynomials symbolically through degree twelve to verify their interior root counts. Run `python checker.py` with the requirements given in `requirements.txt`; the resulting output is included in `check_output.txt`. These finite tests check arithmetic and formulas only; the full all-parameter local conclusion follows from the preceding analytic proof.

## Relationship to prior work
Negative-integral-order polylogarithms and Eulerian rational identities are classical; Miller's 2008 polylogarithm identities and Durán's 2024 discussion of simple negative Eulerian roots establish relevant ingredients, not the varying-real-order kernel-zero crossings or their odd-zeta slopes. Yamamori's 2010 work uses polylogarithms to calculate Bergman kernels and analyze zeros for Fock–Bargmann–Hartogs domains with integer dimension parameters, but does not state the present logarithmic radial-weight family or local transition law. Blaschke's 2011/2012 work on asymptotic Bergman kernels treats a different *boundary-logarithmic* weight \((1-r^2)^\alpha(\gamma+\log(1/(1-r^2)))^\beta\), rather than the origin-logarithmic Mellin weight \((-\log r^2)^{s-1}\). A recent study of genuine Euclidean-distance disk weights \((1-r)^\alpha\) has another exact transition sequence with different moments, so it does not imply the result here. The present theorem combines the integer-order Eulerian zero rigidity with noninteger-order polylogarithmic analytic perturbation and an exclusion proof at the singular boundary point.

## Limitations
The neighborhoods depend on \(m\), and this theorem **does not** give a zero count for every \(s>0\). It does not exclude other zeros for parameters well away from the even integers, and it gives no joint \(m,s\) uniform perturbation width. Established special-function theory already gives the numerator at every integer and several ingredients for the velocity formula, so the new claim is the combined local all-order Bergman-zero census and exact boundary-crossing law. An unindexed prior classification of negative-real-order polylogarithm zeros may still cover part or all of this statement; an independent publication-priority audit has not been performed.

## References
1. S. J. Miller, *An identity for sums of polylogarithm functions*, arXiv:0804.3611v1, publicly posted 2008-04-22; https://arxiv.org/abs/0804.3611.
2. A. Yamamori, *The Bergman kernel of a certain Hartogs domain and the polylogarithm function*, arXiv:1008.5339v1, publicly posted 2010-08-31; https://arxiv.org/abs/1008.5339.
3. A. J. Durán, *Asymptotic for the rightmost zeros of Bell and Eulerian polynomials*, arXiv:2404.03249v1; https://arxiv.org/abs/2404.03249.
4. P. Blaschke, *Asymptotic behavior of Bergman kernels with logarithmic weight*, Journal of Mathematical Analysis and Applications **385** (2012), 293–302, DOI:10.1016/j.jmaa.2011.06.044 (available online 2011-06-22).
5. NIST Digital Library of Mathematical Functions, §§25.2 and 25.12, zeta and polylogarithm continuation formulas; https://dlmf.nist.gov/25.12.
