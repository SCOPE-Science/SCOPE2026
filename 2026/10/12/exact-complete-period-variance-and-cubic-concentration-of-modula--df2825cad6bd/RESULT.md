# Exact complete-period variance and cubic concentration of modular energy

## Finding

For every integer \(m\ge1\), write \(L_m=\operatorname{lcm}(1,\dots,m)\) and let
\[
E_m(n)=\sum_{k=1}^{m}(n\bmod k),\qquad n\in\mathbb Z.
\]
Choose \(N\) uniformly from the \(L_m\) residues \(0,1,\dots,L_m-1\). Then
\[
\mathbb E E_m(N)=\mu_m:=\frac{m(m-1)}4,
\]
and the **complete-period variance** is exactly
\[
\boxed{\operatorname{Var}(E_m(N))=
\frac1{12}\left(\sum_{1\le k,\ell\le m}\gcd(k,\ell)^2-m^2\right)
=\frac1{12}\left(\sum_{d=1}^{m}J_2(d)
\left\lfloor\frac md\right\rfloor^2-m^2\right).}
\]
Here \(J_2(d)=d^2\prod_{p\mid d}(1-p^{-2})\) is the second Jordan totient; \(J_2(1)=1\). As \(m\to\infty\),
\[
\boxed{\operatorname{Var}(E_m(N))=
\frac{2\zeta(2)-\zeta(3)}{36\zeta(3)}m^3
+O(m^2\log(2m)).}
\]
Thus, for each fixed real \(\varepsilon>0\),
\[
\frac1{L_m}\#\left\{0\le n<L_m:
\left|\frac{E_m(n)}{m^2}-\frac14\right|>\varepsilon\right\}
=O_{\varepsilon}(m^{-1}).
\]
The covariance identity behind these conclusions is, for all positive integers \(a,b\),
\[
\boxed{\operatorname{Cov}(N\bmod a,N\bmod b)
=\frac{\gcd(a,b)^2-1}{12},}
\]
where the sample space can equivalently be a complete period modulo \(\operatorname{lcm}(a,b)\).

## Assumptions and scope

All remainders lie in \(\{0,1,\ldots,k-1\}\). All averages and variances use the uniform counting measure on a complete period, not a limit with \(m\) fixed and \(n\to\infty\) at arbitrary rates. The formulas hold for every \(m\ge1\), with variance zero for \(m=1\). The asymptotic and concentration statements take \(m\to\infty\); constants implicit in the variance estimate are absolute, and the concentration constant may depend on \(\varepsilon\).

## Proof

**1. Conditional independence of remainder quotients.** Let \(a,b\ge1\), \(d=\gcd(a,b)\), and choose \(N\) uniformly modulo \(\operatorname{lcm}(a,b)\). Put \(S=N\bmod d\). On conditioning on \(S=s\), write
\[
N\bmod a=s+dA,\qquad N\bmod b=s+dB.
\]
The generalized Chinese remainder theorem identifies the conditional possibilities with all ordered pairs
\(0\le A<a/d\), \(0\le B<b/d\), because \(a/d\) and \(b/d\) are coprime. Consequently \(A\) and \(B\) are independent uniform variables conditional on \(S\), and their conditional means do not depend on \(s\). The law of total covariance therefore gives
\[
\operatorname{Cov}(N\bmod a,N\bmod b)
=\operatorname{Cov}\bigl(S+d\mathbb EA,S+d\mathbb EB\bigr)
=\operatorname{Var}(S)=\frac{d^2-1}{12}.
\]
This argument includes \(a=b\) and \(a=1\) or \(b=1\).

**2. Exact complete-period moments.** Uniformity modulo \(L_m\) implies \(N\bmod k\) is uniform on \(\{0,\dots,k-1\}\); hence its mean is \((k-1)/2\) and \(\mathbb E E_m(N)=m(m-1)/4\). By bilinearity of covariance and step 1,
\[
V_m=\operatorname{Var}(E_m(N))
=\frac1{12}\sum_{k,\ell\le m}
\bigl(\gcd(k,\ell)^2-1\bigr).
\]
Define \(J_2\) by its Euler product above. The identity \(\sum_{d\mid t}J_2(d)=t^2\) follows either from prime powers or Möbius inversion. Applying it to each \(\gcd(k,\ell)\) and interchanging finite sums yields
\[
\sum_{k,\ell\le m}\gcd(k,\ell)^2
=\sum_{d\le m}J_2(d)
\#\{k,\ell\le m:d\mid k,\ d\mid\ell\}
=\sum_{d\le m}J_2(d)\lfloor m/d\rfloor^2.
\]
These are exact finite identities; no probabilistic independence between different moduli is assumed.

**3. Cubic fluctuation constant.** Put \(A(x)=\sum_{d\le x}J_2(d)\) for real \(x\ge1\). Since \(J_2(n)=n^2\sum_{q\mid n}\mu(q)/q^2\), where \(\mu\) denotes the Möbius function,
\[
A(x)=\sum_{q\le x}\mu(q)\sum_{r\le x/q}r^2
=\frac{x^3}{3}\sum_{q\le x}\frac{\mu(q)}{q^3}
+O\left(x^2\sum_{q\le x}\frac1{q^2}\right)
=\frac{x^3}{3\zeta(3)}+O(x^2).
\]
The last step uses the absolutely convergent identity \(\sum_{q\ge1}\mu(q)q^{-3}=1/\zeta(3)\), whose tail contributes \(O(x)\). The identity \(r^2=\sum_{t=1}^{r}(2t-1)\), with all sums finite, gives
\[
\begin{aligned}
\sum_{d\le m}J_2(d)\lfloor m/d\rfloor^2
&=\sum_{t\le m}(2t-1)A(m/t)\\
&=\frac{m^3}{3\zeta(3)}
\sum_{t\le m}\frac{2t-1}{t^3}
+O\left(m^2\sum_{t\le m}\frac{2t-1}{t^2}\right)\\
&=\frac{2\zeta(2)-\zeta(3)}{3\zeta(3)}m^3
+O(m^2\log(2m)).
\end{aligned}
\]
Indeed the tail of \(\sum_{t\ge1}(2t-1)t^{-3}\) contributes only \(O(m^{-1})\), hence \(O(m^2)\) after multiplication by \(m^3\). Subtracting \(m^2\) and dividing by \(12\) proves the stated variance asymptotic.

**4. Concentration.** By Chebyshev's inequality,
\[
\mathbb P\bigl(|E_m(N)-\mu_m|>\tfrac12\varepsilon m^2\bigr)
\le \frac{4V_m}{\varepsilon^2m^4}=O_\varepsilon(m^{-1}).
\]
Because \(\mu_m/m^2=1/4-1/(4m)\), the event in the finding is contained in this event whenever \(m>1/(2\varepsilon)\). This proves the concentration statement.

## Verification

The accompanying standard-library script `verification.py` computes the moments with exact rational arithmetic using three independent representations: direct enumeration over a complete period, the gcd double sum, and the Jordan-totient sum. It checks all three representations for \(1\le m\le9\), all 400 ordered covariance pairs \(1\le a,b\le20\), and both finite formulas for \(1\le m\le150\). Execute `python verification.py` from a directory containing that file; the captured output appears in `verification_output.txt`. The infinite asymptotic is proved above, not inferred from finite experiments.

## Relationship to prior work

En-naoui's September 2025 paper introduced \(E_m(n)\), gave identities, bounds, symmetries and least-common-multiple periodicity, and explicitly identified statistical and analytic behavior as directions for further investigation. Its complete accessible text does not give this covariance law, complete-period variance or cubic asymptotic. Classical Jordan totients and gcd-sum methods supply ingredients for the exact finite identity. Kaltenböck, Kiuchi, Saad Eddin and Ueda (2021) investigate weighted averages of gcd-sum functions; their functions and asymptotic regimes differ from those here. The contribution is the precise second moment and resulting concentration theorem for this modular-energy observable.

## Limitations

The concentration law is a second-moment bound, not a central limit theorem or a quantitative local distribution law. The residue-class sample space is a complete least-common-multiple period; other short sampling intervals are not covered. Classical covariance and Jordan identities make equivalent derivations elsewhere possible; absence in examined sources does not establish an absolute priority claim.

## References

1. E. En-naoui, *The Modular Energy Function: Exact Identities and a Primality Equivalence*, arXiv:2509.10592v1 (first posted September 12, 2025), https://arxiv.org/html/2509.10592v1.
2. L. Kaltenböck, I. Kiuchi, S. Saad Eddin, and M. Ueda, *Sums of Averages of GCD-Sum Functions II*, Results in Mathematics 76, 43 (2021), DOI:10.1007/s00025-021-01357-x, https://link.springer.com/article/10.1007/s00025-021-01357-x.
3. Classical tools used independently: generalized Chinese remainder theorem, Jordan totient divisor identity, Möbius inversion, and Chebyshev's inequality.
