# Exact \(n^{-8}\) term in the Fourier-zero asymptotics of regular polygons

## Finding

Let \(P_{2n}\subset\mathbb R^2\) be the centered regular \(2n\)-gon of area \(\pi\), and define

\[
\kappa(P_{2n})=\operatorname{dist}\!\left(0,\left\{\xi\in\mathbb R^2:\widehat{\mathbf 1_{P_{2n}}}(\xi)=0\right\}\right),
\qquad \widehat f(\xi)=\int_{\mathbb R^2}f(x)e^{i\xi\cdot x}\,dx.
\]

Write \(j=j_{1,1}\) for the first positive zero of the Bessel function \(J_1\). Then, as the integer \(n\to\infty\),

\[
\boxed{\displaystyle
\kappa(P_{2n})=j+\frac{j^3\pi^6}{181440\,n^6}+\frac{j^3\pi^8}{806400\,n^8}+O(n^{-10}).
}
\]

In particular, the exact coefficient of the \(n^{-8}\) term is \(j_{1,1}^3\pi^8/806400\), and the remainder after including it improves to \(O(n^{-10})\).

## Assumptions and scope

The statement concerns centered regular polygons with exactly \(2n\) sides and fixed area \(\pi\). The asymptotic is for \(n\to\infty\); the symbol \(O(n^{-10})\) means a remainder bounded in absolute value by a constant times \(n^{-10}\) for all sufficiently large integers \(n\). No claim is made that the regular dodecagon maximizes \(\kappa\) among all centrally symmetric planar convex bodies.

## Proof

Put \(\delta=\pi/(2n)\) and \(A_n=\sqrt{\delta/\tan\delta}\). On one angular sector, the radial function of \(P_{2n}\) is \(R_n(\theta)=A_n\sec\theta\) for \(|\theta|\le\delta\), extended with period \(2\delta\). Set \(h_n=R_n-1\). Since the polygon and unit disk both have area \(\pi\),

\[
\int_0^{2\pi}\left(h_n(\theta)+\frac{h_n(\theta)^2}{2}\right)d\theta=0. \tag{1}
\]

With \(u=n\theta\), Taylor expansion of \(\sqrt{\delta/\tan\delta}\) and \(\sec(u/n)\) gives, uniformly for \(|u|\le\pi/2\),

\[
h_n(u/n)=n^{-2}G_0(u)+n^{-4}G_1(u)+O(n^{-6}),
\]

where

\[
G_0(u)=\frac{u^2}{2}-\frac{\pi^2}{24},\qquad
G_1(u)=\frac{5u^4}{24}-\frac{\pi^2u^2}{48}-\frac{\pi^4}{640}.
\]

For \(I_k(n)=\int_0^{2\pi}h_n(\theta)^k\,d\theta\), periodicity and the substitution \(u=n\theta\) yield

\[
I_k(n)=2\int_{-\pi/2}^{\pi/2}h_n(u/n)^k\,du.
\]

Consequently,

\[
I_3(n)=\frac{\pi^7}{15120\,n^6}+\frac{13\pi^9}{1209600\,n^8}+O(n^{-10}),\qquad
I_4(n)=\frac{\pi^9}{120960\,n^8}+O(n^{-10}). \tag{2}
\]

For an exact check of these integrals, set \(x=2u/\pi\). Then

\[
G_0=\pi^2\frac{3x^2-1}{24},\qquad G_1=\pi^4\frac{25x^4-10x^2-3}{1920},
\]

and direct polynomial integration on \([-1,1]\) gives

\[
\int_{-1}^1\left(\frac{3x^2-1}{24}\right)^3dx=\frac1{15120},\quad
3\int_{-1}^1\left(\frac{3x^2-1}{24}\right)^2\frac{25x^4-10x^2-3}{1920}\,dx=\frac{13}{1209600},
\]

\[
\int_{-1}^1\left(\frac{3x^2-1}{24}\right)^4dx=\frac1{120960}.
\]

Let \(g(r)=rJ_1(jr)/j\). The Bessel recurrence and derivative identities imply

\[
g(1)=0,\quad g'(1)=g''(1)=J_0(j),\quad g'''(1)=-j^2J_0(j),\quad g''''(1)=-2j^2J_0(j).
\]

Thus, uniformly for small \(h\),

\[
g(1+h)=J_0(j)\left(h+\frac{h^2}{2}-\frac{j^2h^3}{6}-\frac{j^2h^4}{12}\right)+O(h^5). \tag{3}
\]

The radial integral formula for the Fourier transform gives

\[
a_n(j):=\int_{P_{2n}}J_0(j|x|)\,dx=\int_0^{2\pi}g(R_n(\theta))\,d\theta.
\]

Because \(h_n=O(n^{-2})\), the integrated remainder in (3) is \(O(n^{-10})\). Identity (1) cancels the linear and quadratic terms exactly, so (2) gives

\[
a_n(j)=-j^2J_0(j)\left(\frac{I_3(n)}6+\frac{I_4(n)}{12}\right)+O(n^{-10})
=B_0n^{-6}+E_0n^{-8}+O(n^{-10}),
\]

where

\[
B_0=-\frac{j^2J_0(j)\pi^7}{90720},\qquad E_0=-\frac{j^2J_0(j)\pi^9}{403200}.
\]

The Fourier expansion for a regular polygon separates this angular average from its nonconstant harmonics. In a minimizing direction, the remaining harmonic tail at \(\rho=j\) is bounded by a factorial term of the form \(4\pi(jR_n/2)^{2n}/(2n)!\) for all sufficiently large \(n\), hence is \(O(n^{-10})\). Write the full transform in that direction as \(q_n(\rho)\); it follows that

\[
q_n(j)=B_0n^{-6}+E_0n^{-8}+O(n^{-10}). \tag{4}
\]

The nearest-zero direction theorem for regular polygons identifies \(\kappa(P_{2n})\) with the first positive zero of \(q_n\). The established leading-order estimate gives \(\kappa(P_{2n})-j=O(n^{-6})\), while the derivative estimate gives \(q_n'(j)=D_0+O(n^{-4})\), with \(D_0=2\pi J_0(j)/j\ne0\). A Taylor expansion at \(j\), using (4), therefore yields

\[
0=B_0n^{-6}+E_0n^{-8}+D_0(\kappa(P_{2n})-j)+O(n^{-10}).
\]

Finally,

\[
-\frac{B_0}{D_0}=\frac{j^3\pi^6}{181440},\qquad -\frac{E_0}{D_0}=\frac{j^3\pi^8}{806400},
\]

which proves the claimed expansion.

## Verification

The exact rational polynomial integrals in (2) are independently checked by the included standard-library script `verify_asymptotic.py`. The script verifies the rational coefficients only; the analytic proof above supplies the uniform Taylor remainders, the area cancellation, and the reduction to the nearest Fourier zero. The primary paper's certified values for finite \(n\) are consistent with the expansion, but finite numerical values are not used to prove the asymptotic statement.

## Relationship to prior work

Gómez-Serrano, Levitin, Platt, and Polterovich prove the leading term

\[
\kappa(P_{2n})=j_{1,1}+\frac{j_{1,1}^3\pi^6}{181440\,n^6}+O(n^{-8})
\]

and explicitly remark that their numerical data suggest a genuine \(n^{-8}\) term. Their theorem does not state its exact coefficient. The present calculation expands the radial moments one order further and obtains \(j_{1,1}^3\pi^8/806400\), strengthening the remainder to \(O(n^{-10})\). Benguria, Levitin, and Parnovski establish the underlying Fourier-zero functional and disk-perturbation results, while the Bessel identities used here are standard recurrence relations.

## Limitations

This is an asymptotic refinement for regular polygons, not a solution of the global extremal problem for all planar convex bodies. No explicit numerical constant for the \(O(n^{-10})\) remainder is asserted. The argument relies on the cited nearest-zero localization and derivative estimates for the regular polygon; the included script does not certify those analytic inputs. The literature search does not constitute an independent priority certification.

## References

1. J. Gómez-Serrano, M. Levitin, D. Platt, and I. Polterovich, “An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies,” arXiv:2609.10517v1, first submitted 9 September 2026. https://arxiv.org/abs/2609.10517
2. NIST Digital Library of Mathematical Functions, §10.6, “Recurrence Relations and Derivatives,” release 1.2.8, 15 September 2026. https://dlmf.nist.gov/10.6
3. R. Benguria, M. Levitin, and L. Parnovski, “Fourier transform, null variety, and Laplacian’s eigenvalues,” *Journal of Functional Analysis* 257 (2009), 2088–2123. https://arxiv.org/abs/0801.1617
