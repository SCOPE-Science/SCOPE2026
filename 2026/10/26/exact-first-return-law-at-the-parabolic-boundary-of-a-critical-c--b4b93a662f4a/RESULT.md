# Exact first-return law at the parabolic boundary of a critical-cusp map

## Finding

Consider the cusp map
\[
F:[0,1]\longrightarrow[0,1],\qquad F(x)=1-\sqrt{2|x-1/2|}.
\]
Let \(\mu\) have density \(h(x)=2(1-x)\) relative to Lebesgue measure. Put \(J=[1/2,1]\), let \(\mu_J(B)=\mu(B\cap J)/\mu(J)\), and define the first return \(\tau_J(x)=\min\{k\ge1:F^k(x)\in J\}\), with the value \(\infty\) if there is no return. Set
\[
a_0=\frac12,\qquad a_{n+1}=a_n-\frac{a_n^2}{2},\qquad n\ge0.
\]
Then \(\mu\) is invariant, \(\mu(J)=1/4\), and the **entire conditional first-return law** is
\[
\boxed{\mu_J\{\tau_J>n\}=4a_n^2\quad(n=0,1,2,\ldots).}
\]
Consequently, for every integer \(n\ge1\),
\[
\mu_J\{\tau_J=n\}=4a_{n-1}^3-a_{n-1}^4,
\quad \mathbb E_{\mu_J}\tau_J=4,
\]
\[
\lim_{n\to\infty}n^2\mu_J\{\tau_J>n\}=16,
\qquad
\lim_{n\to\infty}n^3\mu_J\{\tau_J=n\}=32.
\]
For every real \(s\ge0\), \(\mathbb E_{\mu_J}[\tau_J^s]<\infty\) if and only if \(s<2\). In particular, the return time is integrable but has infinite second moment.

## Assumptions and scope

The theorem concerns exactly the deterministic, continuous map displayed above, with its specified absolutely continuous invariant probability and the specified half-interval \(J\). Its orbit definition uses the original, undiscounted integer time, not an induced iterate. The endpoint choices affect only \(\mu_J\)-null sets. The map is the parameter \(\vartheta=0\) continuation of the critical square-root family \(f_{\vartheta}(1/2\pm t)=1-\vartheta t-(1-\vartheta/2)\sqrt{2t}\) of Oltiboev and Vafoyev, whose spectral-gap result assumes \(1<\vartheta<2\). The continuation has a parabolic fixed point \(F(0)=0\) with right derivative \(F'(0)=1\), so uniform-expansion conclusions are not assumed at this boundary. The atomic measure \(\delta_0\) is also invariant; no claim of uniqueness among all invariant measures is made.

## Proof

**Inverse branches and invariant density.** The inverse branches on \([0,1]\) are
\[
u(y)=y-\frac{y^2}{2},\qquad v(y)=1-y+\frac{y^2}{2},
\]
with \(u(y)+v(y)=1\) and \(|u'(y)|=|v'(y)|=1-y\) for \(0\le y<1\). Since \(h(x)=2(1-x)\), the transfer operator satisfies, at almost every \(y\),
\[
(\mathcal Ph)(y)=(1-y)\,[h(u(y))+h(v(y))]
=(1-y)\,[4-2(u(y)+v(y))]=2(1-y)=h(y).
\]
The function \(h\) is nonnegative with integral one; therefore \(\mu\) is an invariant probability. Direct integration gives \(\mu(J)=\int_{1/2}^1 2(1-x)\,dx=1/4\).

**Return-time distribution.** The map is strictly increasing on \([0,1/2]\) and satisfies \(F(x)>x\) for \(0<x\le1/2\). The left inverse \(u\) fixes zero, maps \([0,1/2]\) into itself, and is strictly below the identity away from zero. Thus \(a_n=u^{\circ n}(1/2)\downarrow0\). For \(n\ge1\), a point \(x\in J\) avoids \(J\) at times \(1,2,\ldots,n\) if and only if \(y=F(x)\in[0,a_{n-1})\), outside a null set. Indeed, a point of the left branch stays below \(1/2\) for exactly that number of further iterates when its original value falls below the corresponding inverse image \(u^{\circ(n-1)}(1/2)\).

On \(J\), the inverse branch is \(v\). By a change of variables and the exact normalization,
\[
\begin{aligned}
\mu_J\{\tau_J>n\}
&=4\int_0^{a_{n-1}}h(v(y))|v'(y)|\,dy\\
&=8\int_0^{a_{n-1}}u(y)(1-y)\,dy\\
&=4u(a_{n-1})^2=4a_n^2,
\end{aligned}
\]
where the penultimate equality uses \(u'(y)=1-y\) and \(u(0)=0\). For \(n=0\) the identity follows directly from \(4a_0^2=1\). In particular, the tail tends to zero and \(\tau_J\) is finite almost surely. Subtraction of consecutive tails gives
\[
\mu_J\{\tau_J=n\}
=4(a_{n-1}^2-a_n^2)=4a_{n-1}^3-a_{n-1}^4.
\]

**Mean and critical moments.** The recurrence gives \(a_n^2=2(a_n-a_{n+1})\). Tonelli's theorem and telescoping yield the exact mean
\[
\mathbb E_{\mu_J}[\tau_J]=\sum_{n=0}^{\infty}\mu_J\{\tau_J>n\}
=4\sum_{n=0}^{\infty}a_n^2=8(a_0-0)=4.
\]
Also,
\[
\frac1{a_{n+1}}-\frac1{a_n}
=\frac1{2(1-a_n/2)}\longrightarrow\frac12.
\]
Averaging these positive increments gives \(n a_n\to2\). Substitution yields the exact tail constant \(n^2(4a_n^2)\to16\). The point mass satisfies \(4a_{n-1}^3-a_{n-1}^4\sim32n^{-3}\). Therefore for each real \(s>0\), comparison of \(\sum_{n\ge1}n^s\mu_J(\tau_J=n)\) with \(\sum_{n\ge1}n^{s-3}\) yields finiteness if and only if \(s<2\). The case \(s=0\) is immediate.

## Verification

The complete proof above uses exact inverse branches, an exact invariant density, one integral and one scalar recurrence. The standalone file `verify.py`, runnable with Python 3 and no third-party dependencies, tests the transfer identity at 858 rational test points, checks eleven exact rational tail values against the antiderivative, and checks a large-index numerical consequence of \(n a_n\to2\). Its recorded result is `VERIFY_OK exact_transfer_grid=858 exact_return_tails=11 asymptotic_steps=100000`. These tests are not substitutes for the all-index proof.

## Relationship to prior work

Oltiboev and Vafoyev (2026), Section 3, study the critical-exponent square-root cusp family for \(1<\vartheta<2\), where their formula (3.2) provides uniform expansion. Their paper proves Sobolev regularity and analytic response and does not supply this parameter-zero first-return distribution. The exact parabolic boundary statement here is neither obtained by their spectral gap nor asserted to extend their regularity theorem to neutral maps.

Coates, Luzzatto and Muhammad (2022, revised 2024) develop induced maps, return-tail estimates and statistical limit theorems for a broad, generally different full-branch intermittent class. Their results motivate looking at power-law tails but do not specify the finite-time law of this right-half return problem. General intermittent return-tail theory is not claimed as novel; the precise parameter-boundary invariant density, exact all-index law, sharp constant and complete moment threshold are the contribution.

## Limitations

This result is confined to a single canonical parameter boundary and a specified return interval and measure. It neither supplies a full spectral analysis of the parabolic map nor proves mixing or decay of correlations. Historical literature may contain the same map under another parametrization; the available searches and inspected sources do not conclusively establish priority. The 2026 preprint on random cusp systems by Oltiboev, Rakhimov and Ruziboev was accessible in abstract only, leaving a source-inspection limitation. Independent validation has not been performed.

## References

Oltiboev, D., and Vafoyev, F. (2026), *Critical cusp cancellation and analytic response for a Bernoulli random interval map*, arXiv:2610.23180v1, submitted 16 October 2026, https://arxiv.org/abs/2610.23180 (especially Section 3, equations (3.1)–(3.4)).

Coates, D., Luzzatto, S., and Muhammad, M. (2022/2024), *Doubly Intermittent Full Branch Maps with Critical Points and Singularities*, arXiv:2209.12725v2, https://arxiv.org/abs/2209.12725 (especially Sections 1.1–1.3, 2.2, 4.1).

Oltiboev, D., Rakhimov, K., and Ruziboev, M. (2026), *Linear response for random systems with a cusp*, arXiv:2608.26969, https://arxiv.org/abs/2608.26969 (abstract only available for this comparison).
