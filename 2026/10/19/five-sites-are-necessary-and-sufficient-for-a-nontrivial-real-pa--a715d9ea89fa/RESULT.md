# Five sites are necessary and sufficient for a nontrivial real Pauli pair on the integer line

## Finding

Let \(f,g:\mathbb Z\to\mathbb R\) be finitely supported. Their *Pauli data* comprise all coordinate magnitudes \(|f(n)|\) and all continuous-frequency Fourier magnitudes
\[
 |\widehat f(\theta)|=\left|\sum_{n\in\mathbb Z}f(n)e^{in\theta}\right|,\qquad \theta\in\mathbb R.
\]
Call two sequences *trivially associated* if one is a global sign or a signed translated reflection of the other (translation may be zero). Then any two sequences with identical Pauli data and at most four nonzero coordinates are trivially associated. The minimum cardinality of the common support of a nontrivial real Pauli pair is exactly five.

For every \(t\in\mathbb R\setminus\{0\}\) and \(u\in\mathbb R\setminus\{0,1,-1\}\), the coefficient vectors
\[
 f=(1,t,u-1,ut,-u),\qquad g=(-1,t,1-u,ut,u)
\]
are nontrivial Pauli partners supported on \(\{0,1,2,3,4\}\). In particular, \(u=2\), \(t=1\) gives \(f=(1,1,1,2,-2)\), \(g=(-1,1,-1,2,2)\).

## Assumptions and scope

The coefficient field is \(\mathbb R\), the underlying group is the infinite integer line \(\mathbb Z\), and the Fourier magnitude is known at **every** real torus frequency, not merely on a finite cyclic sampling grid. No spacing assumption is made on supports of size at most four. Equality of coordinate magnitudes forces the two supports to coincide. The equivalence relation permits \(g(n)=\epsilon f(n)\) or \(g(n)=\epsilon f(h-n)\) for an integer \(h\) and \(\epsilon\in\{+1,-1\}\); ordinary translations cannot produce distinct partners with the same finite nonempty coordinate support. This equivalence is deliberately broader than global-sign equivalence, so the claim is not produced by reflection.

## Proof

**Autocorrelation reduction.** Write the shared support in increasing order as \(S=\{s_0<\cdots<s_{m-1}\}\), with nonzero real amplitudes \(a_j=f(s_j)\). Coordinatewise magnitude equality gives \(g(s_j)=\epsilon_j a_j\), where \(\epsilon_j\in\{+1,-1\}\). Changing the global sign of \(g\), assume \(\epsilon_0=1\). Equality of squared Fourier magnitudes is equivalent, coefficient by coefficient, to equality of all aperiodic autocorrelations
\[
 C_f(d)=\sum_{s_j-s_i=d}a_i a_j,\qquad d\in\mathbb N.
\]
Consequently, for each positive lag \(d\),
\[
 \sum_{\substack{i<j:\ s_j-s_i=d\\\epsilon_i\ne\epsilon_j}}a_i a_j=0. \tag{1}
\]
As the maximal lag \(s_{m-1}-s_0\) occurs for exactly one unordered pair, (1) forces \(\epsilon_{m-1}=\epsilon_0=1\) when \(m\ge2\). In (1), every summand is nonzero; hence a lag occurring exactly once among the cross-sign pairs is impossible.

**One and two sites.** There is no interior site and the endpoints have the same sign, so \(g=f\) after global-sign normalization.

**Three sites.** Write consecutive gaps \(a=s_1-s_0>0\) and \(b=s_2-s_1>0\). The only possibly different sign pattern is \((+,-,+)\), with cross-sign lags \(a,b\). To avoid a singleton cross-sign lag, necessarily \(a=b\). Then (1) at lag \(a\) becomes \(a_1(a_0+a_2)=0\). Since \(a_1\ne0\), we have \(a_2=-a_0\). Reflection of \(f\) about the support midpoint, followed by global sign reversal, is precisely \(g\). Thus every three-site partner is trivial.

**Four sites: one interior sign flip.** Set \(a=s_1-s_0\), \(b=s_2-s_1\), \(c=s_3-s_2\), all positive. If just \(s_1\) is flipped, the three cross-sign pair distances are \(a,b,b+c\). Since \(b+c>b\), these three cannot all agree; at least one distance occurs just once. This contradicts (1). If just \(s_2\) is flipped, the distances are \(a+b,b,c\) and the same argument applies.

**Four sites: both interior signs flipped.** The cross-sign distances are \(a,a+b,b+c,c\). Since \(a+b>a\) and \(b+c>c\), they cannot all be equal; because no lag may occur exactly once, they must split into two equal pairs. The only feasible pairing is \(a=c\) and \(a+b=b+c\): the alternative \(a=b+c\), \(a+b=c\) is impossible because \(a+b>a\ge c\), and pairings equating \(a\) to \(a+b\) are impossible. Hence the support is reflection symmetric. The two autocorrelation equations are
\[
 a_0a_1+a_2a_3=0,\qquad a_0a_2+a_1a_3=0. \tag{2}
\]
All amplitudes are nonzero. Substitution or elimination in (2) yields \(a_3^2=a_0^2\). If \(a_3=a_0\), then \(a_2=-a_1\) and \(g\) is exactly the reflection of \(f\); if \(a_3=-a_0\), then \(a_2=a_1\) and \(g\) is minus the reflection of \(f\). No nontrivial four-site pair exists.

**Five-site construction.** Form the real-coefficient polynomials
\[
 F(z)=(1+uz^2)(1+tz-z^2),\qquad
 G(z)=(1+uz^2)(-1+tz+z^2).
\]
The two degree-two factors \(1+tz-z^2\) and \(-1+tz+z^2\) are related by polynomial reversal: \(-1+tz+z^2=z^2(1+t/z-1/z^2)\). Thus for \(|z|=1\), their moduli agree, and therefore \(|F(z)|=|G(z)|\). Expanding gives the advertised five coefficients, whose absolute values coincide term by term. The parameter exclusions ensure that all five coefficients are nonzero. Moreover \(|f(0)|=1\ne |u|=|f(4)|\), so the shared modulus profile is not reflection symmetric: a signed reflection cannot associate these partners. They are not equal up to overall sign because the constant and linear coefficients have incompatible signs. This proves sharpness.

## Verification

`verify.py` checks the five-term construction over 64 nondegenerate integer parameter pairs by exact autocorrelations and checks all four-site-or-smaller integer supports in \(\{0,\ldots,9\}\), with amplitudes in \(\{-2,-1,1,2\}\), comparing exact cross-sign partner data. This supplementary finite computation is not used in the universal proof. Run it with `python verify.py`; it requires only Python's standard library. The analytic proof above covers arbitrary supports, arbitrary gaps and arbitrary nonzero real amplitudes.

## Relationship to prior work

Shkarin's 2013 *On Pauli Pairs*, Lemma 4.1 and Proposition 4.2, gives autocorrelation equations and a classification of **complex-valued four-step functions on four consecutive equal intervals**. The reduction to autocorrelations is established there and is credited. The present result specifically treats real coefficients with **arbitrary four-site gaps on the integer line**, and determines the **least support cardinality five** with an explicit entirely real witness; the cited proposition does not state this arbitrary-gap, sharp real threshold.

Novikov and Xu's April 2026 *On Phase Retrieval for Continuous and Discrete Fourier Transforms* develops general constructions of Pauli partners in arbitrary dimensions via finite-difference operators (notably Theorem 2 and Example 2). It establishes nonuniqueness but does not determine the sharp real coefficient support threshold on \(\mathbb Z\). The five-site example here uses the classical polynomial-reversal mechanism, not a claim of invention of zero-flipping.

Ramos and Sousa (2024) and Lysen (2026) address recovery of *global* Pauli data from data sampled at sparse sets of real frequencies under analytic decay hypotheses. Their discrete sampling schemes and Gaussian-decay conclusions neither imply nor classify the finite-support real sign ambiguity considered here.

## Limitations

This is a theorem about real coefficients, full continuous-frequency Fourier intensity and one-dimensional infinite-lattice supports; it does not classify arbitrary complex coefficients, sampled cyclic DFT problems or the number of inequivalent partner pairs above five sites. The construction is not asserted to classify all possible five-site pairs. The self-review does not constitute independent validation. Historical-priority risk remains for unindexed real-valued finite Pauli-pair classifications predating the cited literature.

## References

1. S. Shkarin, *On Pauli pairs*, Journal of Mathematical Physics **54** (2013), DOI 10.1063/1.4794087; arXiv:1209.1225. Relevant material: §4, Lemma 4.1 and Proposition 4.2.
2. R. G. Novikov and T. Xu, *On Phase Retrieval for Continuous and Discrete Fourier Transforms*, arXiv:2604.25662v1 (public April 28, 2026). Relevant material: §§1–4, especially Theorem 2.
3. J. P. G. Ramos and M. Sousa, *On Pauli pairs and Fourier uniqueness problems*, arXiv:2410.12065v1 (October 15, 2024). Relevant material: Introduction and Theorems 1–2.
4. T. K. Lysen, *Discrete Pauli pairs*, arXiv:2605.23079v1 (May 21, 2026). Relevant material: Introduction, definitions and main results.
