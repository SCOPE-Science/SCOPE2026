# Corrected critical-feedback equation and a three-halves edge law in feedback-trained recurrent networks

## Result

Consider the quasi-static dynamical mean-field transition studied in Varun Vaidya, *Learning-Induced Dynamical Transition in Recurrent Neural Networks*, arXiv:2609.19288v1, with normalized output \(\hat y\), gain \(g>1\), standard Gaussian measure \(Dz\), and activation \(\phi(x)=\tanh x\).

The source's marginal-stability condition is
\[
1=g^2\int Dz\,\phi'(\sqrt{u_c}\,z)^2.
\]
The stationary self-consistency condition inherited from the preceding DMFT equation and effective potential is
\[
\boxed{
 u_c=g^2\int Dz\,\phi(\sqrt{u_c}\,z)^2+\hat y_c^2.
}
\tag{1}
\]
In the displayed Eq. (4.6) of arXiv:2609.19288v1 the factor \(z\) is absent from the argument of \(\phi\). Equation (1) is the condition obtained directly by setting the two-time plateau equal to its equal-time value in Eqs. (4.2)--(4.3). The omission is also numerically material: at \(g=1.3\), combining the printed formula literally with the source's marginal condition gives \(\hat y_c^2<0\), whereas (1) gives \(\hat y_c=0.195822866873\), consistent with the source's reported value \(\hat y_c\approx0.2\).

Define
\[
F(u)=\mathbb E\,\operatorname{sech}^4(\sqrt u Z),\qquad
G(u)=\mathbb E\,\tanh^2(\sqrt u Z),\qquad Z\sim N(0,1).
\]
Then the corrected critical point is parametrized by
\[
 g^2F(u_c)=1,\qquad \hat y_c^2=u_c-g^2G(u_c).
\tag{2}
\]
Since \(F\) is strictly decreasing on \((0,\infty)\), the first equation has a unique positive solution \(u_c(g)\) for each \(g>1\).

Let
\[
r=g^2-1.
\]
The Gaussian Taylor expansions are
\[
F(u)=1-2u+7u^2-\frac{94}{3}u^3+\frac{502}{3}u^4+O(u^5),
\]
\[
G(u)=u-2u^2+\frac{17}{3}u^3-\frac{62}{3}u^4+O(u^5).
\]
Solving (2) order by order gives
\[
\boxed{
 u_c=\frac r2+\frac{3r^2}{8}-\frac{7r^3}{48}+\frac{39r^4}{128}+O(r^5)
}
\tag{3}
\]
and, more importantly,
\[
\boxed{
 \hat y_c^2=\frac{r^3}{6}-\frac{r^4}{8}+\frac{31r^5}{160}+O(r^6).
}
\tag{4}
\]
Writing \(\varepsilon=g-1\), the order-\(\varepsilon^4\) term cancels and therefore
\[
\boxed{
 \hat y_c
 =\frac{2}{\sqrt3}\,\varepsilon^{3/2}
 \left(1+\frac65\varepsilon^2+O(\varepsilon^3)\right),
 \qquad g\downarrow1.
}
\tag{5}
\]
Thus the critical learned feedback vanishes with a three-halves power at the chaos edge. The source paper establishes that \(\hat y_c\) increases with \(g\) numerically; (5) identifies its sharp onset exponent and coefficient.

The same cancellation has a simple local origin. For any smooth odd activation normalized as
\[
\phi(x)=x-a x^3+b x^5+O(x^7),\qquad a>0,
\]
the two critical equations imply
\[
\hat y_c^2=\frac{(g^2-1)^3}{18a}+O((g^2-1)^4),
\]
so
\[
\hat y_c=\frac{2}{3\sqrt a}(g-1)^{3/2}(1+O(g-1)).
\]
For \(\tanh x\), \(a=1/3\), recovering the leading coefficient in (5). This general expansion is included as an explanation of the cancellation; the source-specific claims concern the model and critical equations of arXiv:2609.19288v1.

## Target-amplitude feasibility boundary

For a constant target \(A\), the source's quasi-static construction assumes successful learning makes \(\hat y(t)\) increase monotonically from \(0\) to
\[
q=\frac{A}{\sqrt N}.
\]
Consequently, within that construction a necessary condition for the learning trajectory to cross the freezing bifurcation is
\[
q\ge \hat y_c(g).
\]
For small normalized targets this produces the explicit edge law
\[
\boxed{
 g_{\mathrm{edge}}(q)
 =1+\left(\frac34\right)^{1/3}q^{2/3}+O(q^2),
 \qquad q\downarrow0.
}
\tag{6}
\]
Hence a target much smaller than \(\sqrt N\) cannot suppress chaos unless the untrained network is correspondingly close to the \(g=1\) onset: the allowable excess gain is only of order \(q^{2/3}\).

For the source's choice \(q=1\), direct Gaussian quadrature of (2) gives a numerical crossing \(\hat y_c=1\) at
\[
 g\approx1.855589101139.
\]
This last number is a numerical consequence of the corrected quasi-static equations, not an independently certified threshold for the finite-size learning dynamics.

## Proof of the three-halves law

Set \(r=g^2-1\). From \(F(u_c)=1/(1+r)\), substitution of the Taylor series for \(F\) gives (3). Substituting that expansion into
\[
\hat y_c^2=u_c-(1+r)G(u_c)
\]
produces (4). Since \(r=2\varepsilon+\varepsilon^2\), one obtains
\[
\hat y_c^2=\frac43\varepsilon^3+\frac{16}{5}\varepsilon^5+O(\varepsilon^6),
\]
which yields (5). Equation (6) follows by inversion.

For the general odd activation, Gaussian moments give
\[
\mathbb E\phi'(\sqrt u Z)^2
 =1-6au+3(9a^2+10b)u^2+O(u^3),
\]
\[
\mathbb E\phi(\sqrt u Z)^2
 =u-6au^2+15(a^2+2b)u^3+O(u^4).
\]
Solving the marginal equation through second order and substituting in the self-consistency equation cancels all dependence on \(b\) at leading nonzero order, leaving \(\hat y_c^2=r^3/(18a)+O(r^4)\).

## Relation to prior work

Sompolinsky--Crisanti--Sommers established the dynamical mean-field transition to chaos in random recurrent networks. The source paper itself notes that its marginal condition is the SCS condition, now crossed dynamically by learned feedback. Suppression of chaotic activity by external forcing is also established prior art, including Rajan--Abbott--Sompolinsky (2010), which computes critical input amplitudes for periodically driven random networks. Those general phenomena are not claimed as new here.

The contribution claimed here is narrower: correction of the source-specific stationary critical equation as required by its own preceding DMFT equations, the resulting exact near-edge expansion of the learned critical feedback, and the target-amplitude feasibility law for the learning trajectory described in arXiv:2609.19288v1. Searches for the source title, critical-feedback formulation, equivalent near-edge scaling, and relevant prior SCOPE records did not locate an earlier statement of this source-specific combination. Older random-network literature could contain an algebraically equivalent static-input expansion, so broad priority for the exponent itself is not claimed.

## Limitations

The result is a theorem about the source paper's quasi-static DMFT critical equations. It does not prove that a finite network undergoes a sharp dynamical transition at the same point, and it inherits the source approximation that central-time derivatives are negligible on the fast correlation scale. The numerical value \(g\approx1.855589101139\) is floating-point quadrature/root finding, not an interval-certified constant. The correction to Eq. (4.6) is inferred from Eqs. (4.2)--(4.3) and from consistency with the reported \(g=1.3\) critical feedback; no claim is made about authorial intent beyond that mathematical inconsistency.
