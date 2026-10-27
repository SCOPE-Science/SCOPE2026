# All-order arithmetic-progression correlations and sharp rigidity for the period-doubling subshift

## Finding

Let \(s_n=(-1)^{\nu_2(n+1)}\) for integers \(n\geq0\), where \(\nu_2\) is the exponent of two in a positive integer. This is the balanced sign coding of the fixed point of the period-doubling substitution \(0\mapsto01\), \(1\mapsto00\). For any integer progression length \(m\geq1\) and step \(h\geq1\), the correlation

\[
C_m(h)=\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}\prod_{j=0}^{m-1}s_{n+jh}
\]

exists. Write \(a=\nu_2(h)\). Define rational numbers \(c_m\) by \(c_0=1\), \(c_1=1/3\), and, for \(k\geq1\),

\[
c_{2k}=(-1)^k c_k,\qquad
c_{2k+1}=\frac{(-1)^{k+1}c_{k+1}+(-1)^k c_k}{2}.
\]

Then the complete family of arithmetic-progression correlations is

\[
\boxed{C_m(h)=\begin{cases}
1-2^{-a}(1-c_m),&m\text{ even},\\[2pt]
\frac13+(-\frac12)^a(c_m-\frac13),&m\text{ odd}.
\end{cases}}
\]

These formulas are valid for every \(m\geq1\) and every positive \(h\), with no restriction on the odd part of \(h\). The sharp all-order inequality and equality classification are

\[
\boxed{|c_m|\leq\frac13\quad(m\geq1),\qquad
|c_m|=\frac13\ \Longleftrightarrow\ m=2^r\ \text{or}\ m=3\cdot2^r\quad(r\geq0).}
\]

The signs in the equality cases are \(c_1=1/3\), \(c_{2^r}=-1/3\) for \(r\geq1\), \(c_3=-1/3\), and \(c_{3\cdot2^r}=1/3\) for \(r\geq1\). In particular, every even order \(m\geq2\) exhibits an exact spacing-parity gap:

\[
|C_m(h)|\leq\frac13\ (h\text{ odd}),\qquad
C_m(h)\geq\frac13\ (h\text{ even}).
\]

Equality in the latter lower bound holds precisely when \(\nu_2(h)=1\) and \(m\) is a power of two greater than one.

## Assumptions and scope

The sequence is the one-sided period-doubling fixed point with symbol \(0\) coded as \(+1\) and symbol \(1\) as \(-1\), starting at index zero. We use only positive integer spacings and nonempty arithmetic progressions; repeated sites are excluded by positivity of \(h\). The value of the auxiliary function at the single two-adic integer zero is irrelevant to all integrals, because that singleton has Haar measure zero. All asymptotic averages are ordinary one-sided Cesàro limits; unique ergodicity of the underlying primitive substitution is consistent with, but not needed for, the elementary existence argument below.

## Proof

**1. Passage to a two-adic integral.** Let \(\mathbb Z_2\) denote the two-adic integers with normalized additive Haar probability measure \(\mu\). Away from zero, set \(f(x)=(-1)^{\nu_2(x)}\). For each fixed finite collection of integer translations, approximate the translated functions by their values modulo \(2^L\): the approximation agrees except when at least one translated argument is divisible by \(2^L\). The union of these exceptional cylinder sets has Haar measure at most \(m2^{-L}\), and the same upper asymptotic density among positive integers. Since the nonexceptional cylinder product is periodic modulo \(2^L\), passage to \(L\to\infty\) proves existence of the Cesàro limit and its identity with

\[
C_m(h)=\int_{\mathbb Z_2}\prod_{j=0}^{m-1}f(x+jh)\,d\mu(x).
\]

The change from the original \(n\) to \(x=n+1\) simply translates the averaging variable.

**2. Reduction to the odd step.** Write \(h=2^a u\) with \(u\) odd. Multiplication by \(u\) preserves normalized Haar measure and the two-adic valuation. For \(a=0\), substitution \(x=uy\) therefore yields \(C_m(u)=c_m\), where

\[
c_m=\int_{\mathbb Z_2}\prod_{j=0}^{m-1}f(x+j)\,d\mu(x).
\]

For general \(a\), partition by whether \(2^a\mid x\). On the complement, \(\nu_2(x+jh)=\nu_2(x)\) for all \(j\), so the product equals \(1\) if \(m\) is even and equals \(f(x)\) if \(m\) is odd. The subgroup \(2^a\mathbb Z_2\) has measure \(2^{-a}\); writing \(x=2^ay\) inside it gives \((-1)^{am}c_m\) conditionally, because the odd multiplier \(u\) may be removed by Haar invariance. For odd \(m\), the complementary integral is

\[
\sum_{r=0}^{a-1}\frac{(-1)^r}{2^{r+1}}=\frac13\bigl(1-(-1/2)^a\bigr).
\]

Combining the two pieces proves both displayed formulas, including \(a=0\).

**3. Exact length recursion.** For \(x\in\mathbb Z_2\), \(f(2x)=-f(x)\) away from a null set and \(f(2x+1)=1\). Split the definition of \(c_{2k}\) into the even and odd classes of the integration variable. In each class precisely \(k\) factors have even arguments, each contributing a minus sign, and after halving the even arguments the surviving factors are \(k\) consecutive translates. Translation invariance thus gives \(c_{2k}=(-1)^k c_k\). For \(2k+1\) factors, the even integration class has \(k+1\) even arguments, while the odd integration class has \(k\). Their contributions are \((-1)^{k+1}c_{k+1}\) and \((-1)^k c_k\), with equal probability, yielding the second recurrence. Since \(\mu(\nu_2(x)=r)=2^{-r-1}\),

\[
c_1=\sum_{r\geq0}\frac{(-1)^r}{2^{r+1}}=\frac13.
\]

This proves the recursion for all lengths and uniquely determines its rational values.

**4. Global sharp bound and equality.** Induct on \(m\). The even recurrence preserves absolute value under halving, and the odd recurrence bounds \(|c_{2k+1}|\) by the average of \(|c_k|\) and \(|c_{k+1}|\). Thus \(|c_m|\leq1/3\) for all positive \(m\). Direct recurrence gives

\[
(c_1,c_2,c_3,c_4,c_5,c_6,c_7)
=(1,-1,-1,-1,0,1,0)/3.
\]

Let \(E=\{2^r:r\geq0\}\cup\{3\cdot2^r:r\geq0\}\). The even recurrence gives equality in the bound at even index exactly when it holds at half that index. For any odd \(m=2k+1\geq5\), equality would force both \(k\) and \(k+1\) to be sharp indices. Inductively these must be consecutive elements of \(E\). Its only consecutive pairs are \((1,2)\), \((2,3)\), and \((3,4)\). Since \(k\geq2\), the remaining cases give \(m=5\) or \(m=7\), whose correlations are zero. Conversely \(1,3\) are sharp, and the even recurrence propagates sharpness to every index in \(E\). The signs follow by the same recurrence.

**5. Sharp spacing-parity gap.** For even \(m\), an odd step has \(a=0\), hence \(C_m(h)=c_m\). For an even step, \(a\geq1\) and the first formula with \(c_m\geq-1/3\) gives \(C_m(h)\geq1-\frac43 2^{-a}\geq1/3\). Equality requires \(a=1\) and \(c_m=-1/3\), which the established sign classification makes equivalent to a positive power-of-two order.

## Verification

The supplied standalone `verify.py` implements the rational recurrences directly and constructs finite-cylinder approximations independently from the defining valuations. Its checked outputs were: 4,096 exact recurrence values, 24 predicted sharp-order indices within that range, 256 independent finite-cylinder tests, and the even-order spacing inequality for 2,048 lengths. For cylinder modulus \(2^L\), the discrepancy from the true correlation is bounded by \(2m/2^L\), because at most \(m\) exceptional residue classes can contain a vanishing translated argument and each product changes by at most two. These checks corroborate the proof; the unrestricted statements rest on the two-adic integral and induction, not on finite enumeration.

## Relationship to prior work

Baake and Grimm's analyses of the period-doubling model set (arXiv:0909.5605 and arXiv:1007.0707) identify its two-adic structure and determine the two-point autocorrelation. Indeed, their two-point identity is exactly the \(m=2\) specialization here, \(C_2(h)=1-4/(3\cdot2^{\nu_2(h)})\). Deng and Moody (arXiv:0904.4552) provide general higher-point model-set correlation formulas, which establish a framework but do not in their inspected theorems evaluate all consecutive arithmetic progressions of the period-doubling sign sequence or classify the sharp orders. Baake and Grimm's broader diffraction survey (arXiv:1105.0095) and Špitalský's recurrence analysis (arXiv:1807.09096) address other correlation or symbolic-recurrence invariants. The specific contribution assessed here is the two-parameter all-order evaluated recurrence and the sharp equality set and parity gap, not existence of general higher correlations or the previously known two-point formula.

## Limitations

The theorem addresses equally spaced spatial samples of the balanced period-doubling sequence. It does not evaluate general irregularly spaced higher correlations, arbitrary substitution sequences, or diffraction beyond the known two-point setting. A general model-set correlation integral can yield these values after additional specialization; historical priority of this evaluated specialization cannot be conclusively established from searchable sources alone.

## References

1. M. Baake and U. Grimm, *Surprises in aperiodic diffraction*, arXiv:0909.5605v1 (public 2009-09-30), especially Section 2, period-doubling example. https://arxiv.org/abs/0909.5605
2. M. Baake and U. Grimm, *Diffraction of limit periodic point sets*, arXiv:1007.0707v1 (public 2010-07-05), especially Section 3, equations (8)–(10). https://arxiv.org/abs/1007.0707
3. X. Deng and R. V. Moody, *Weighted model sets and their higher point-correlations*, arXiv:0904.4552v1 (public 2009-04-29), especially Sections 2–3. https://arxiv.org/abs/0904.4552
4. M. Baake and U. Grimm, *Kinematic diffraction from a mathematical viewpoint*, arXiv:1105.0095v1 (public 2011-04-30), especially Section 4. https://arxiv.org/abs/1105.0095
5. V. Špitalský, *Recurrence quantification analysis of the period-doubling sequence*, arXiv:1807.09096v1 (public 2018-07-24), Introduction and Theorems 1–2. https://arxiv.org/abs/1807.09096
