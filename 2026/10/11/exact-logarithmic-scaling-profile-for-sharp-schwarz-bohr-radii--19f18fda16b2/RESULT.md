# Exact logarithmic scaling profile for sharp Schwarz–Bohr radii

## Finding

For \(0<p\le2\), let \(R_{k,m,p}\) be the sharp radius \(R_{1,k,m,p}\) from the recent Schwarz-mapping Bohr theorem, so that \(R_{k,m,p}\in(0,1)\) is the unique solution of
\[
p\frac{1-R^m}{1+R^m}
=
\frac{2R^{2k}}{1-R^{2k}},
\qquad
k,m\in\mathbb N.
\]

For every \(\lambda>0\), define \(s_p(\lambda)>0\) by
\[
p\tanh\!\left(\frac{\lambda s_p(\lambda)}2\right)
=
\frac{2}{e^{2s_p(\lambda)}-1}.
\]
Then
\[
R_{k,m,p}
=
\exp\!\left[
-\frac{s_p(m/k)}{k}
\right].
\]

Thus the apparent two-integer dependence of the sharp radius collapses exactly: in logarithmic radius coordinates, \(k\) supplies only the overall scale and the shape is controlled by the single ratio \(m/k\).

The profile is continuous and strictly decreasing, and its two extreme regimes are
\[
\lim_{\lambda\to\infty}s_p(\lambda)
=
\frac12\log\!\left(1+\frac2p\right)
\]
and
\[
s_p(\lambda)
\sim
\frac12
W\!\left(\frac{8}{p\lambda}\right)
\qquad
(\lambda\downarrow0),
\]
where \(W\) is the principal Lambert function.

Consequently, for every sequence of positive integers with
\[
k_j\to\infty,
\qquad
\frac{m_j}{k_j}\to\lambda\in(0,\infty),
\]
one has the sharp-radius scaling limit
\[
k_j\left(1-R_{k_j,m_j,p}\right)
\longrightarrow
s_p(\lambda).
\]

There is also an exact elementary ray. If \(m=2k\), then
\[
R_{k,2k,p}
=
\left(
\frac{p}{p+1+\sqrt{4p+1}}
\right)^{1/(2k)}.
\]
For example,
\[
R_{k,2k,2}=3^{-1/(2k)}.
\]

## Assumptions and scope

The radius \(R_{k,m,p}\) is precisely the sharp radius denoted \(R_{1,k,m,p}\) in Theorem 3.1 of arXiv:2610.02935v1. The theorem assumes
\[
k,m\in\mathbb N,
\qquad
0<p\le2.
\]

The result concerns the sharp root itself and therefore applies wherever that source theorem uses the same radius, including its JB-star-triple extension.

No statement is made outside the source range \(0<p\le2\), and no claim is made about the other root families appearing elsewhere in the source.

## Proof

Put
\[
R=e^{-s/k},
\qquad
\lambda=\frac{m}{k}.
\]
Then
\[
R^m=e^{-\lambda s},
\qquad
R^{2k}=e^{-2s}.
\]
Therefore
\[
\frac{1-R^m}{1+R^m}
=
\tanh\!\left(\frac{\lambda s}{2}\right)
\]
and
\[
\frac{2R^{2k}}{1-R^{2k}}
=
\frac{2}{e^{2s}-1}.
\]
The source root equation is therefore equivalent, exactly, to
\[
p\tanh\!\left(\frac{\lambda s}{2}\right)
=
\frac{2}{e^{2s}-1}.
\]

For fixed \(p\) and \(\lambda\), the left side is strictly increasing from \(0\) to \(p\) as \(s\) runs from \(0\) to \(+\infty\). The right side is strictly decreasing from \(+\infty\) to \(0\). Hence there is exactly one positive solution \(s_p(\lambda)\), and
\[
R_{k,m,p}
=
e^{-s_p(m/k)/k}.
\]

If \(\lambda_2>\lambda_1\), then at every fixed \(s>0\),
\[
\tanh\!\left(\frac{\lambda_2s}{2}\right)
>
\tanh\!\left(\frac{\lambda_1s}{2}\right).
\]
Since the right side is decreasing in \(s\), the unique intersection for \(\lambda_2\) lies strictly to the left of that for \(\lambda_1\). Thus \(s_p\) is strictly decreasing. Continuity follows from strict monotonicity in \(s\) and continuity of the defining equation.

As \(\lambda\to\infty\), monotonicity gives a limit \(L\ge0\). The limit cannot be zero because the right side then diverges, so \(L>0\). Hence
\[
\tanh\!\left(\frac{\lambda s_p(\lambda)}2\right)\longrightarrow1.
\]
Passing to the defining equation gives
\[
p=\frac{2}{e^{2L}-1},
\]
and therefore
\[
L=\frac12\log\!\left(1+\frac2p\right).
\]

Now let \(\lambda\downarrow0\). If \(s_p(\lambda)\) stayed bounded, the left side would tend to zero while the right side stayed positive, which is impossible. Thus
\[
s_p(\lambda)\to+\infty.
\]
Moreover,
\[
\lambda s_p(\lambda)\to0.
\]
Indeed, if some subsequence satisfied
\[
\lambda s_p(\lambda)\ge\varepsilon>0,
\]
then the left side of the defining equation would be bounded below by
\[
p\tanh(\varepsilon/2)>0,
\]
whereas its right side would tend to zero because \(s_p(\lambda)\to\infty\).

Consequently,
\[
\tanh\!\left(\frac{\lambda s}{2}\right)
\sim
\frac{\lambda s}{2}
\]
and
\[
\frac{2}{e^{2s}-1}
\sim
2e^{-2s}.
\]
The defining equation becomes
\[
\frac{p\lambda s}{2}
\sim
2e^{-2s},
\]
or equivalently
\[
(2s)e^{2s}
\sim
\frac{8}{p\lambda}.
\]
By inversion with the principal Lambert function,
\[
2s_p(\lambda)
\sim
W\!\left(\frac{8}{p\lambda}\right).
\]

For the scaling limit, continuity gives
\[
s_p(m_j/k_j)\to s_p(\lambda).
\]
Since
\[
R_{k_j,m_j,p}
=
\exp\!\left[
-\frac{s_p(m_j/k_j)}{k_j}
\right],
\]
the elementary limit
\[
k(1-e^{-a/k})\to a
\]
yields
\[
k_j(1-R_{k_j,m_j,p})\to s_p(\lambda).
\]

Finally, set \(\lambda=2\) and
\[
y=e^{-2s}=R^{2k}.
\]
Since
\[
\tanh s=\frac{1-y}{1+y},
\]
the defining equation becomes
\[
p\frac{1-y}{1+y}
=
\frac{2y}{1-y},
\]
or
\[
p(1-y)^2=2y(1+y).
\]
Its unique root in \((0,1)\) is
\[
y
=
\frac{p}{p+1+\sqrt{4p+1}}.
\]
Taking the \(2k\)-th root proves the balanced-ray formula.

## Verification

The recent primary source was inspected at Theorem 3.1, its proof of uniqueness and sharpness, its numerical table for \(R_{1,k,m,p}\), and the later JB-star-triple theorem that reuses exactly the same radius.

The change of variables
\[
s=-k\log R,
\qquad
\lambda=m/k
\]
was checked directly against the source equation. Independent numerical root checks over representative values of
\[
p\in\{1/2,1,2\}
\]
and
\[
\lambda\in\{0.05,0.2,1,2,10\}
\]
confirmed the transformed equation and the balanced-ray closed form. These numerical checks are sanity checks only; the proof is analytic.

For small \(\lambda\), numerical comparison with
\[
\frac12W\!\left(\frac{8}{p\lambda}\right)
\]
was also used only as a sanity check. The asymptotic follows from the proved facts
\[
s_p(\lambda)\to\infty
\]
and
\[
\lambda s_p(\lambda)\to0.
\]

## Relationship to prior work

The 2026 primary source proves that its radius is the unique sharp root of the displayed algebraic-transcendental equation and gives sample numerical values. It does not state a logarithmic scaling collapse, a profile depending only on \(m/k\), a Lambert-\(W\) regime, or the balanced-ray closed form.

A January 2026 paper on sharp Bohr--Rogosinski radii for Schwarz functions studies a related but different root family. It gives separate limits as one integer parameter tends to infinity, rather than the simultaneous ratio scaling of the present theorem.

Earlier Bohr--Rogosinski work likewise studies sharp roots and limiting radii for other coefficient patterns. Targeted searches for the exact source radius, the ratio \(m/k\), logarithmic rescaling, and Lambert-\(W\) asymptotics did not locate a statement implying the present profile.

## Limitations

The result is an exact analysis of one sharp-radius family from the source. It does not compare all of the paper's distinct Bohr-radius equations.

The Lambert-\(W\) statement is asymptotic as
\[
\lambda\downarrow0;
\]
it is not an exact closed form for general \(\lambda\).

The simultaneous limit assumes
\[
m/k\to\lambda\in(0,\infty).
\]
The boundary regimes
\[
m/k\to0
\quad\text{or}\quad
m/k\to\infty
\]
are described through the profile limits rather than by a single uniform remainder estimate.

## References

1. N. Sarkar and P. Das, *Refined Bohr inequalities and Bohr radii involving Schwarz mappings for holomorphic functions in Banach spaces and JB-star-triples*, arXiv:2610.02935v1, 2026.
2. M. B. Ahamed, S. Majumder, and N. Sarkar, *Sharp Bohr-Rogosinski radii for Schwarz functions and Euler operators in \(\mathbb C^n\)*, arXiv:2601.06630v1, 2026.
3. I. R. Kayumov, D. M. Khammatova, and S. Ponnusamy, *Bohr--Rogosinski phenomenon for analytic functions and Cesaro operators*, Journal of Mathematical Analysis and Applications 496 (2021), 124824.
