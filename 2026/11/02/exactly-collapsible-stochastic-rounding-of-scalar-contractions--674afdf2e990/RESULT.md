# Exactly collapsible stochastic rounding of scalar contractions

## Finding

Consider ideal, unbiased stochastic rounding to the **fixed integer lattice**. Write \(\mathcal R(x)\) for the integer-valued random variable with distribution
\[
\Pr\{\mathcal R(x)=\lfloor x\rfloor\}=1-\{x\},\qquad
\Pr\{\mathcal R(x)=\lfloor x\rfloor+1\}=\{x\},
\]
where \(\{x\}=x-\lfloor x\rfloor\); when \(x\) is an integer the output is that integer surely. Every rounding event below is sampled independently conditional on the current integer state.

For \(0<q<1\), \(k\in\mathbb Z_{\ge0}\), define \(X_0=k\) and
\[
 X_{j+1}\mid X_j\ \sim\ \mathcal R(qX_j),\qquad j\ge0.
\]
Then the following are equivalent:

1. For every integer \(k\ge0\) and every integer \(n\ge1\), \(X_n\) has the same distribution as **one** stochastic rounding \(\mathcal R(q^n k)\).
2. The preceding equality in distribution holds for every \(k\ge0\) already at \(n=2\).
3. \(q=1/b\) for some integer \(b\ge2\).

More strongly, for any integer sequence \(b_1,\ldots,b_n\ge2\), rounding after each successive contraction by \(1/b_j\) has exactly the distribution
\[
 \mathcal R\!\left(\frac{k}{b_1\cdots b_n}\right).
\]
The terminal distribution is independent of the order of these reciprocal-integer contractions, although the intermediate trajectories need not be.

For a fixed \(b\ge2\), let \(\mu_n=k/b^n\) and \(\theta_n=\{\mu_n\}\). In particular,
\[
 \mathbb E X_n=\mu_n,\quad
 \Pr(X_n=\lfloor\mu_n\rfloor+1)=\theta_n,\quad
 \operatorname{Var}(X_n)=\theta_n(1-\theta_n).
\]
Among **all** integer-valued random variables with mean \(\mu_n\), this variance is the minimum possible; equality characterizes support on the two adjacent integers around the mean. For every contraction \(q\in(0,1)\) not equal to a reciprocal integer, some starting state already has strictly greater variance at the second step than this lattice minimum.

For \(k\ge1\), let \(\tau=\inf\{n\ge0:X_n=0\}\) and choose the least integer \(L\ge0\) for which \(b^L\ge k\). Then the reciprocal-integer chain has the exact extinction law
\[
 \Pr(\tau>n)=
 \begin{cases}
 1,&0\le n<L,\\
 k/b^n,&n\ge L,
 \end{cases}\qquad
 \mathbb E\tau=L+\frac{k/b^L}{1-1/b}.
\]
In particular \(\tau<\infty\) almost surely.

## Assumptions and scope

The lattice \(\mathbb Z_{\ge0}\) is unbounded upward and contains zero; no overflow, underflow, finite mantissa, or accumulated error in multiplication by \(q\) is modeled. The operation \(\mathcal R\) uses *exact* unbiased probabilities, not equal-probability rounding. An independent fresh rounding draw is used at every transition. All stated distributions are for deterministic integer initial states and nonnegative contractive slopes. A physical grid of spacing \(\Delta>0\) is obtained by multiplying states and standard deviations by \(\Delta\) and variances by \(\Delta^2\).

This is the idealized fixed-grid implementation of scalar forward Euler for \(y'=-\lambda y\) with exact unrounded amplification \(q=1-\lambda h\in(0,1)\), followed by one stochastic rounding of the full update. It is **not** a claim about IEEE operation-wise floating-point arithmetic, which has nonuniform spacing and may round intermediate arithmetic.

## Proof

**Unbiasedness.** For every real \(x\), \(\mathbb E\mathcal R(x)=x\). Conditional expectation therefore gives \(\mathbb E[X_{j+1}\mid X_j]=qX_j\), hence \(\mathbb E X_n=q^nk\) for all \(q\in(0,1)\).

**Reciprocal-integer closure.** Suppose an integer-valued random variable \(Y\) is supported on \(\{m,m+1\}\), with mean \(\mu\in[m,m+1]\). Write \(m=ba+r\) with integers \(a\ge0\) and \(0\le r\le b-1\). Dividing either \(m\) or \(m+1\) by \(b\) and stochastically rounding produces values only in \(\{a,a+1\}\). This remains true at both endpoints \(r=0\) and \(r=b-1\) because rounding an exact integer leaves it fixed. The result's mean is \(\mu/b\), which lies in \([a,a+1]\). A distribution on these two adjacent integers with that mean is unique and equals \(\mathcal R(\mu/b)\). Thus the operation maps the law \(\mathcal R(\mu)\) exactly to the law \(\mathcal R(\mu/b)\). Starting with \(\mathcal R(k)=k\) proves the fixed-\(b\) claim by induction; applying the same argument successively with distinct integer denominators proves the order-independent product law.

**Sharp converse.** Let \(q\in(0,1)\) and suppose \(1/q\) is not an integer. Put \(m=\lfloor1/q\rfloor\). Then \(mq<1<(m+1)q\), with \(m\ge1\). The open interval \((m/q,(m+1)/q)\) has length \(1/q>1\), so it contains a positive integer \(k\). Consequently \(m<kq<m+1\), and the first rounded state has positive probability at each of \(m\) and \(m+1\). From \(m\), the second transition has positive probability at zero and one, because \(0<mq<1\). From \(m+1\), it has positive probability at one and two, because \(1<(m+1)q<2\). Therefore \(X_2\) has positive mass at **all three** integers \(0,1,2\). One rounding \(\mathcal R(kq^2)\) can be supported on at most two adjacent integers. The distributions differ, disproving condition 2. Conditions 1 and 2 are plainly related by implication, and the reciprocal-integer proof establishes the remaining implication.

**Sharp variance.** If \(Z\) takes integer values and has finite second moment and mean \(\mu\), set \(m=\lfloor\mu\rfloor\). The pointwise inequality \((Z-m)(Z-m-1)\ge0\) gives
\[
 \operatorname{Var}(Z)\ge(\mu-m)(m+1-\mu)
 =\{\mu\}(1-\{\mu\}).
\]
Equality holds exactly when \(Z\in\{m,m+1\}\) almost surely. The previously proved two-point law reaches equality at every time for reciprocal integers. For the nonreciprocal witness, the three strictly positive masses make the inequality strict (regardless of whether \(\mu=kq^2\) lies above or below one).

**Extinction time.** Since zero is absorbing, \(\{\tau>n\}=\{X_n\ge1\}\). For \(n<L\), \(k/b^n>1\), so the adjacent-integer support lies in the positive integers and survival is certain. For \(n\ge L\), \(0<k/b^n\le1\), and the support is \(\{0,1\}\); survival probability is the Bernoulli parameter \(k/b^n\). Summing the survival probabilities proves the geometric-series formula for \(\mathbb E\tau\) and the almost-sure extinction assertion.

**Concrete strictness example.** At \(q=2/5\) with \(k=6\), two independently rounded steps give
\[
 \Pr(X_2=0,1,2)=(3/25,20/25,2/25),\quad
 \operatorname{Var}(X_2)=124/625.
\]
A single rounding of the same unrounded mean \(6(2/5)^2=24/25\) gives masses \((1/25,24/25)\) at zero and one and variance \(24/625\). Thus intermediate rounding inflates terminal variance by the exact factor \(31/6\) here.

## Verification

The standalone rational-arithmetic enumeration in `verify.py` checks \(7100\) reciprocal-integer fixed-step instances, \(208\) variable-denominator instances, \(130\) nonreciprocal rational contraction witnesses, and the explicit variance example. Reproduce with `python3 verify.py` using the Python standard library alone. Its output is `VERIFY_OK exact_fixed 7100 variable 208 nonreciprocal_witness 130 variance_example 124/625`. These finite checks are diagnostics only: the preceding support, expectation, and lattice inequalities constitute the proof for all admissible parameters.

## Relationship to prior work

Croci and Giles analyze low-precision rounding in numerical time stepping of heat equations and prove probabilistic rounding-error bounds. Their 2020 public preprint supplies both the motivating numerical setting and the standard unbiased-rounding definition. The later survey by Croci, Fasi, Higham, Mary, and Mikaitis describes the unbiased nearest-neighbor mode and numerical ODE applications. Dahlqvist, Salvia, and Constantinides provide a general compositional probabilistic analysis of rounding errors. None of the inspected relevant passages states the reciprocal-integer *if-and-only-if* collapse of all iterated output laws, the variable-denominator closure, or its sharp scalar extinction law. This is a statement-level comparison rather than an assertion that a search proves uniqueness; an independently discovered specialized formula may exist.

## Limitations

The results rely critically on ideal unbiased fixed-grid rounding, exact real multiplication before rounding, a scalar positive contraction, and independent fresh rounding. They do not extend without fresh analysis to variable-spacing IEEE formats, stochastic rounding with finite random precision, matrix systems, additive forcing, or noncontractive and sign-changing updates. The minimal-variance statement compares integer-valued *marginal laws with a prescribed mean*, not pathwise errors, total simulation costs, or any general optimality of a finite-precision implementation. No independent scientific audit has been performed.

## References

1. M. Croci and M. B. Giles, *Effects of round-to-nearest and stochastic rounding in the numerical solution of the heat equation in low precision*, arXiv:2010.16225, first public 2020-10-30. https://arxiv.org/abs/2010.16225
2. M. Croci, M. Fasi, N. J. Higham, T. Mary, and M. Mikaitis, *Stochastic rounding: implementation, error analysis and applications*, Royal Society Open Science 9 (2022), 211631. https://pmc.ncbi.nlm.nih.gov/articles/PMC8905452/
3. F. Dahlqvist, R. Salvia, and G. A. Constantinides, *A Probabilistic Approach to Floating-Point Arithmetic*, arXiv:1912.00867 (2019). https://arxiv.org/abs/1912.00867
