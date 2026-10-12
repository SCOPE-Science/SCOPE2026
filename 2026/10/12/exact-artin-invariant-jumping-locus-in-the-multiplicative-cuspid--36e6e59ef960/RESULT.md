# Exact Artin-invariant jumping locus in the multiplicative cuspidal Kummer family
## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). Consider the multiplicative Kummer surfaces constructed by Kondō and Schröer from
\[
\delta=(\lambda_4u^{-4}+\lambda_2u^{-2}+\lambda_0)D_{u^{-1}}+(\mu_4v^{-4}+\mu_2v^{-2}+\mu_0)D_{v^{-1}}+\tau(uD_u+vD_v),
\]
under \(\lambda_4\mu_4\tau\ne0\). Define
\[
\Delta=\lambda_4\mu_2^3+\mu_4\lambda_2^3.
\]
Then the Artin invariant of the minimal-resolution K3 surface is
\[
\sigma=\begin{cases}
1,&(\lambda_2,\mu_2)=(0,0),\\
2,&\Delta=0\text{ and }(\lambda_2,\mu_2)\ne(0,0),\\
3,&\Delta\ne0.
\end{cases}
\]
Thus \(\sigma\) is independent of \(\lambda_0,\mu_0\) and of the chosen nonzero \(\tau\). For fixed nonzero \(\lambda_4,\mu_4\), the middle stratum consists of three punctured lines through the origin, indexed by the three cube roots \(\alpha\) of \(\mu_4/\lambda_4\), and the common origin is the unique \(\sigma=1\) point in this coefficient slice.

## Assumptions and scope
The ground field is algebraically closed of characteristic \(2\). The claim is about the multiplicative branch \(G\cong\mu_2\) of the Kondō--Schröer construction, so \(\tau\ne0\), and normality is imposed through \(\lambda_4\mu_4\ne0\). The statement is made in the displayed vector-field coefficient parameterization; it does not assert that these coordinates form a global coarse-moduli chart.

The Artin invariant is the integer \(\sigma\) determined by \(\operatorname{disc}\operatorname{Pic}(X)=-2^{2\sigma}\) for the supersingular K3 surface \(X\).

## Proof
Kondō--Schröer reduce the rational sections of one quasielliptic fibration to common solutions \(\alpha\) of
\[
\lambda_4\alpha^4+\mu_4\alpha=0,
\qquad
\lambda_2\alpha^2+\mu_2\alpha=0.
\]
If there are \(2^m\) such \(\alpha\)'s, with \(0\le m\le2\), their lattice computation gives \(\sigma=3-m\).

Both equations have the solution \(\alpha=0\). If \((\lambda_2,\mu_2)=(0,0)\), the second equation imposes no further condition and the first becomes
\[
\alpha(\lambda_4\alpha^3+\mu_4)=0.
\]
Because \(\lambda_4\mu_4\ne0\), the cubic has three distinct nonzero roots over \(k\). Hence there are four common solutions, so \(m=2\) and \(\sigma=1\).

Now assume \((\lambda_2,\mu_2)\ne(0,0)\). A nonzero common solution forces both \(\lambda_2\) and \(\mu_2\) to be nonzero, and the second equation then forces uniquely
\[
\alpha=\frac{\mu_2}{\lambda_2}.
\]
Substitution into the first equation gives
\[
\lambda_4\left(\frac{\mu_2}{\lambda_2}\right)^4+\mu_4\frac{\mu_2}{\lambda_2}
=
\frac{\mu_2}{\lambda_2^4}\bigl(\lambda_4\mu_2^3+\mu_4\lambda_2^3\bigr)
=
\frac{\mu_2}{\lambda_2^4}\Delta.
\]
Therefore a nonzero common solution exists exactly when \(\Delta=0\). In that case there are exactly two common solutions, \(0\) and \(\mu_2/\lambda_2\), so \(m=1\) and \(\sigma=2\). If \(\Delta\ne0\), only \(0\) survives, so \(m=0\) and \(\sigma=3\).

For fixed \(\lambda_4,\mu_4\), the equation \(\Delta=0\) away from the origin is equivalent to
\[
\left(\frac{\mu_2}{\lambda_2}\right)^3=\frac{\mu_4}{\lambda_4}.
\]
An algebraically closed field of characteristic \(2\) contains three distinct cube roots of every nonzero scalar, giving the three punctured lines. The coefficient equations determining \(m\) contain neither \(\lambda_0\), \(\mu_0\), nor the value of the nonzero \(\tau\), proving the asserted independence.

## Verification
The accompanying verifier checks the decisive symbolic substitution identity
\[
\lambda_2^4\left(\lambda_4(\mu_2/\lambda_2)^4+\mu_4(\mu_2/\lambda_2)\right)
=
\mu_2\Delta.
\]
The root counts in the proof are algebraic, not inferred from finite sampling: the cubic \(\lambda_4\alpha^3+\mu_4\) is separable because its roots are nonzero and its derivative is \(\lambda_4\alpha^2\) in characteristic \(2\). Running `python artifacts/verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Kondō--Schröer prove that the multiplicative construction yields supersingular K3 surfaces with \(1\le\sigma\le3\), derive \(\sigma=3-m\), and state that every \(m\in\{0,1,2\}\) occurs. Their proof describes generic and extreme choices but does not state the exact coefficient locus for each Artin invariant. The calculation above closes that gap by eliminating \(\alpha\) and identifying the single cubic jumping equation \(\Delta=0\), together with its deeper origin and its three-line decomposition after fixing \(\lambda_4,\mu_4\).

Focused searches using the source identifier, the coefficient names, the Artin-invariant values, the cubic relation, and parameter-locus aliases found no published statement implying this exact stratification. A later paper on K3 surfaces of Kummer type in characteristic two is a residual comparison risk, but targeted searches did not expose an equivalent coefficient formula.

## Limitations
The result classifies the Artin invariant in the source's vector-field coefficient presentation. It does not identify which of the source's abstract index-two or index-four overlattices occur, and it does not construct a global quotient of this coefficient space by reparameterization. The claim is restricted to \(G\cong\mu_2\) and does not treat the additive \(\alpha_2\) branch.

## References
1. Shigeyuki Kondō and Stefan Schröer, “Kummer surfaces associated with group schemes”, arXiv:1912.12015, first submitted 27 December 2019; especially Proposition 2.1, Corollary 2.2, Proposition 3.5, and Theorem 5.2.
2. Igor Dolgachev, “K3 surfaces of Kummer type in characteristic two”, *Bulletin of the London Mathematical Society* 56 (2024), 1903–1919, for later context on Kummer-type configurations in characteristic two.
