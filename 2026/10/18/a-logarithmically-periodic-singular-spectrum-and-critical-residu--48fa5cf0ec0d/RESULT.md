# A logarithmically periodic singular spectrum and critical residue for a Cantor moment commutator

## Finding
Let \(\mu\) be the symmetric middle-thirds Cantor probability measure on \([0,1]\), let \(H^2\) be the analytic Hardy Hilbert space with orthonormal monomials \(e_n(z)=z^n\) for \(n\ge0\), and define the dilation average \((Mf)(z)=\int_0^1 f(tz)\,d\mu(t)\). Let \(S\) be multiplication by \(z\), and \(C=SM-MS\). Set \(d=\log 2/\log 3\), \(\rho=(1+d)^{-1}\), and
\[
F(y)=\prod_{j=1}^{\infty}\frac{1+e^{-2y/3^j}}2,\qquad P(y)=\prod_{k=0}^{\infty}(1+e^{-2\cdot3^k y}),\qquad
K(y)=-y^{d+1}\frac{d}{dy}\bigl(F(y)P(y)\bigr),\quad 1\le y\le3.
\]
The products and their derivatives converge locally uniformly for \(y>0\); \(K\) is positive, continuously differentiable, and \(K(3)=K(1)\). For every integer \(n\ge1\), put \(y_n=n/3^{\lfloor\log_3 n\rfloor}\in[1,3)\). Then the singular values of \(C\), in nonincreasing order, obey the **uniform sharp oscillatory law**
\[
\boxed{\quad n^{d+1}s_n(C)=K(y_n)+O(n^{-1})\quad(n\to\infty).\quad}
\]
The profile \(K\) is **nonconstant**: certified rational interval arithmetic gives
\[
0.4641231655<K(1)<0.4641231678,\qquad
0.4614025831<K(2)<0.4614026195.
\]
Hence \(n^{d+1}s_n(C)\) has no limit, though it has the exact logarithmically periodic profile above. In particular \(C\in\mathcal S_p\) **exactly when** \(p>\rho\), and \(C\in\mathcal S_{\rho,\infty}\setminus\mathcal S_\rho\).

Despite the absence of an ordinary Weyl coefficient, the *critical logarithmic spectral residue* exists:
\[
\boxed{\quad
\lim_{N\to\infty}\frac1{\log N}\sum_{n=1}^N s_n(C)^\rho
=\frac1{\log3}\int_1^3 K(y)^\rho\,\frac{dy}{y}>0.\quad}
\]
Consequently \(|C|^\rho\) is a measurable weak-trace-class positive compact operator, and every Dixmier trace of it equals the displayed integral. The result is confined to the specified Cantor measure and moment-dilation average; no arbitrary-fractal extension is claimed.

## Assumptions and scope
The Cantor measure is the distribution of \(T=\sum_{j\ge1}2B_j/3^j\) for independent equally likely binary digits \(B_j\). By symmetry \(U=1-T\) has the same law. The dilation-average operator is bounded because every \(f\mapsto f(tz)\) is a contraction on \(H^2\). The notation \(\mathcal S_{p,\infty}\) means the compact weak Schatten ideal, characterized by \(\sup_n n^{1/p}s_n<\infty\) for \(p>0\). Singular values are indexed from \(1\); \(e_n\) is indexed from \(0\).

## Proof
**(1) Exact singular values and ordering.** The moments \(a_n=\int t^n\,d\mu(t)\) satisfy \(Me_n=a_ne_n\). Thus \(Ce_n=(a_n-a_{n+1})e_{n+1}\), with strictly positive weights
\[
w_n=a_n-a_{n+1}=\mathbb E[U(1-U)^n],\quad n\ge0.
\]
They strictly decrease because the integrand decreases for \(0<U<1\), which has full measure. Therefore \(s_n(C)=w_{n-1}\) **exactly**. In particular \(C\) is compact.

**(2) Self-similar Laplace law.** The Laplace transform \(F(t)=\mathbb E[e^{-tU}]\) has the infinite product above. By factoring its first \(m\) factors and reindexing, for \(y\in[1,3]\),
\[
F(3^m y)=2^{-m}F(y)P_m(y),\qquad
P_m(y)=\prod_{k=0}^{m-1}(1+e^{-2\cdot3^k y}).
\]
The products \(P_m\) converge to \(P\) with all derivatives at a super-exponential rate, uniformly on \([1,3]\). Differentiating gives
\[
-F'(3^m y)=3^{-m(d+1)}\bigl(-(FP_m)'(y)\bigr).
\]
It follows uniformly in the phase \(y\) that \(-t^{d+1}F'(t)=K(y)+O(e^{-ct})\) for some \(c>0\). This proves positivity and periodic compatibility at \(y=1,3\). Repeating the differentiation proves \(F^{(j)}(t)=O(t^{-d-j})\) for every fixed integer \(j\ge0\) and \(t\ge1\).

**(3) From Laplace to exact moments.** On \(0\le u\le1/2\) the elementary logarithm bounds imply
\[
0\le e^{-nu}-(1-u)^n\le2nu^2e^{-nu}.
\]
After multiplication by \(u\) and Cantor integration, the discrepancy between \(w_n\) and \(-F'(n)\) is at most \(2n\mathbb E[U^3e^{-nU}]+O(e^{-n/2})=O(n^{-d-2})\), by the third derivative bound from (2). Replacing \(n\) with \(n-1\) changes the rescaled expression by \(O(n^{-1})\), because the continuous phase profile is \(C^1\). Thus the asserted singular-value formula holds uniformly.

**(4) Nonconstant oscillation and ideal threshold.** All factors defining \(K\) are positive, and the product has a bounded strictly positive minimum on \([1,3]\). The independent rational-enclosure checker uses signed Taylor upper/lower bounds for \(e^{-x}\), controls omitted Cantor digits by \(3^{-18}\), and bounds the missing outer product from \(k=4\) by \(2^{-162}\). It certifies the disjoint rational intervals printed above; in particular \(K(1)>K(2)+10^{-3}\). Along \(n=3^m\) and \(n=2\cdot3^m\), the rescaled singular values have distinct limits. The two-sided power bounds yield exactly the Schatten threshold.

**(5) Critical trace.** Let \(q=\rho\). The uniform \(O(n^{-1})\) error and positivity imply
\[
s_n(C)^q=\frac{K(y_n)^q}{n}+O(n^{-2}).
\]
The periodic function \(x\mapsto K(3^{\{x\}})^q\) is continuous and Lipschitz. Comparing the harmonic sum with its logarithmic integral yields
\[
\sum_{n=1}^N\frac{K(y_n)^q}{n}
=\frac{\log N}{\log3}\int_1^3 K(y)^q\frac{dy}{y}+O(1).
\]
This establishes the displayed limit and hence equality of all Dixmier traces by their defining generalized-limit construction on the normalized logarithmic singular-value sums.

## Verification
Run `python3 check_fractal.py` from the directory containing the packaged files. The program uses only Python's standard library and exact rational arithmetic, bounds the exponential by alternating Taylor polynomial intervals, and proves \(K(1)-K(2)>0.001\). The displayed decimal endpoints are rounded outward from rational enclosures. This independently checks the nonconstant-profile certificate, not the infinite-dimensional theorem; the latter follows from Steps (1)–(5).

## Relationship to prior work
Liflyand's 2013 survey develops Hausdorff moment sequences and composition-based averaging operators on Hardy spaces. Dovgoshey, Martio, Ryazanov and Vuorinen (2006), Theorem 6.11, reproduce an earlier exact log-periodic **ordinary moment** asymptotic for the Cantor measure; their Proposition 6.15 gives its Laplace product. Both are expressly treated here as **prior work**. An ordinary moment asymptotic with a multiplicative \(1+o(1)\) error does not control the smaller first difference \(a_n-a_{n+1}\); the derivative-sensitive, quantified singular-value law, its demonstrated nonconstant profile, and the resulting exact critical noncommutative residue require the separate argument above. This is not a claim that Cantor moment oscillations or the Laplace product were previously unknown.

## Limitations
No first-difference claim is made for general self-similar measures, unequal digit weights, or arbitrary measures. The critical trace is a logarithmically averaged spectral invariant; the ordinary rescaled singular-value sequence has no limit. This is a self-review, not an independent audit. Prior literature may contain an equivalent derivative-level Cantor-moment asymptotic not located by the searches. The checker certifies only specified rational inequalities and cannot independently establish the asymptotic proof.

## References
1. E. Liflyand, *Hausdorff operators on Hardy spaces*, Eurasian Math. J. 4 (2013), 101–141; published 2013-12-30, https://emj.enu.kz/index.php/main/article/view/558 (particularly Sections 2–3).
2. O. Dovgoshey, O. Martio, V. Ryazanov, M. Vuorinen, *The Cantor function*, Expositiones Mathematicae 24 (2006), 1–37, https://doi.org/10.1016/j.exmath.2005.05.002 (Theorem 6.11 and Proposition 6.15).
