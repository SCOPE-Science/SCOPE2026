# Sharp boundary regularity and exact dyadic profiles for clipped random quadratic dynamics

## Finding
Consider the state-dependent random choice between \(f_0(z)=z^2\) and \(f_1(z)=z^2/2\) with the clipped affine feedback defined below. For every \(0<\alpha<1\), \(0<\varepsilon<1/2\), and initial state \(p\in[\varepsilon,1-\varepsilon]\), the escape-probability function has the **same exact, sharp boundary exponent** at radii \(1\) and \(2\):
\[
\gamma_\varepsilon=\frac{-\log(1-\varepsilon)}{\log 2}.
\]
The exponent is independent of the feedback strength \(\alpha\) and the initial state. More precisely, sufficiently near either boundary the escape probability (near radius \(1\)) or its deficit from one (near radius \(2\)) is bounded above and below by positive constants times the radial distance to that boundary raised to \(\gamma_\varepsilon\); no larger pointwise Hölder exponent is possible.

There is a stronger **exact finite-level renormalization**. Both boundaries have one common dyadic shape function \(H_{\alpha,\varepsilon}\) after a finite number of all-zero or all-one steps, and their remaining state dependence is only a positive multiplicative prefactor. For \(\alpha=1/2\), \(\varepsilon=1/4\), this shape is not a power law: the normalized endpoint quotient has at least two distinct accumulation values.

## Assumptions and scope
Fix \(0<\alpha<1\), \(0<\varepsilon<1/2\), and put \(b=1-\alpha\), \(p_+=1-\varepsilon\), \(p_-=\varepsilon\). At state \(p\in[p_-,p_+]\), choose a digit \(X_{j+1}\in\{0,1\}\) with conditional probability \(\mathbb P(X_{j+1}=1\mid p_j)=p_j\). Update
\[
p_{j+1}=\operatorname{clip}_{[p_-,p_+]}(bp_j+\alpha X_{j+1}),\qquad p_0=p,
\]
where \(\operatorname{clip}_{[a,c]}(v)=\max(a,\min(c,v))\). Starting with \(z_0=z\in\mathbb C\), apply \(z_{j+1}=f_{X_{j+1}}(z_j)\), where \(f_0(z)=z^2\) and \(f_1(z)=z^2/2\). Write \(E_p(r)\) for the probability that \(|z_j|\to\infty\) when \(|z_0|=r\). The radial law does not depend on the initial argument of \(z\).

Define \(R=\sum_{j\ge1}X_j2^{-j}\) under the law started from state \(p\), and define one universal shape
\[
H_{\alpha,\varepsilon}(u)=\mathbb P_{p_+}(R\ge1-u),\qquad 0\le u\le1.
\]
For all-one and all-zero digit paths let
\[
p_j^+=\min(p_+,1-b^j(1-p)),\qquad p_j^-=\max(p_-,b^jp),\qquad j\ge0,
\]
with saturation indices \(n_+(p)=\min\{j\ge0:p_j^+=p_+\}\) and \(n_-(p)=\min\{j\ge0:p_j^-=p_-\}\). Both indices are finite. Set
\[
C_+(p)=\frac{\prod_{j=0}^{n_+(p)-1}p_j^+}{p_+^{n_+(p)}},\qquad
C_-(p)=\frac{\prod_{j=0}^{n_-(p)-1}(1-p_j^-)}{p_+^{n_-(p)}}.
\]
Empty products equal one. Both constants are strictly positive.

**Exact identities.** For all integers \(n\ge n_+(p)\) and \(0\le u\le1\),
\[
1-E_p\!\left(2^{1-2^{-n}u}\right)
=C_+(p)p_+^n H_{\alpha,\varepsilon}(u).
\tag{1}
\]
For all integers \(n\ge n_-(p)\) and \(0\le u\le1\),
\[
E_p\!\left(2^{2^{-n}u}\right)
=C_-(p)p_+^n H_{\alpha,\varepsilon}(u).
\tag{2}
\]
These are finite-level equalities, not merely asymptotic formulas.

**Sharp radial estimates.** There exist \(c,C,\eta>0\), depending only on \(\alpha,\varepsilon\), such that for every \(p\in[p_-,p_+]\),
\[
 c(r-1)^{\gamma_\varepsilon}\le E_p(r)\le C(r-1)^{\gamma_\varepsilon}
 \quad(1<r<1+\eta),
\]
\[
 c(2-r)^{\gamma_\varepsilon}\le 1-E_p(r)\le C(2-r)^{\gamma_\varepsilon}
 \quad(2-\eta<r<2).
\tag{3}
\]
For any fixed permitted initial state, neither bound remains valid as an upper bound with a larger exponent.

**Nonconstant endpoint profile at explicit parameters.** When \(\alpha=1/2\), \(\varepsilon=1/4\),
\[
H_{1/2,1/4}(1)=1,\qquad H_{1/2,1/4}(3/4)=\frac{27}{32},\qquad
\frac{27/32}{(3/4)^{\log_2(4/3)}}<1.
\tag{4}
\]
Thus \((1-E_{3/4}(2^{1-\delta}))/\delta^{\gamma_{1/4}}\) has different limits along \(\delta=2^{-n}\) and \(\delta=(3/4)2^{-n}\). By symmetry, the analogous normalized quotient at radius \(1\) also fails to converge when started at state \(1/4\).

## Proof
**1. Reduction to a binary distribution.** For \(r>0\), put \(t=\log_2 r\). After \(n\) updates, the logarithmic radius is
\[
\log_2|z_n|=2^n\left(t-\sum_{j=1}^n X_j2^{-j}\right).
\]
If \(t>R\), this tends to \(+\infty\); if \(t<R\), it tends to \(-\infty\). If \(t=R\), the displayed quantity is the dyadic tail in \([0,1]\), so it does not produce escape. Any fixed binary word of length \(n\) has probability at most \((1-\varepsilon)^n\), hence an individual infinite word has probability zero. Since each real number has at most two binary expansions, \(R\) has no atoms. Consequently, for \(0<t<1\),
\[
E_p(2^t)=\mathbb P_p(R<t)=\mathbb P_p(R\le t).
\tag{5}
\]
The endpoint probabilities are \(E_p(1)=0\) and \(E_p(2)=1\).

**2. Prefix-factorization lemma.** For \(n\ge0\) and \(0\le u\le1\), the event \(R\ge1-2^{-n}u\) requires the first \(n\) digits to be one, up to a null dyadic-boundary event. On that event
\[
R=1-2^{-n}+2^{-n}R^{\mathrm{tail}},
\]
where the conditional tail is distributed as the full binary sum started from state \(p_n^+\). Thus, with \(Q_n^+(p)=\prod_{j=0}^{n-1}p_j^+\),
\[
\mathbb P_p(R\ge1-2^{-n}u)
=Q_n^+(p)\,\mathbb P_{p_n^+}(R\ge1-u).
\tag{6}
\]
Similarly, the event \(R\le2^{-n}u\) requires the first \(n\) digits zero, up to null boundary events, so with \(Q_n^-(p)=\prod_{j=0}^{n-1}(1-p_j^-)\),
\[
\mathbb P_p(R\le2^{-n}u)
=Q_n^-(p)\,\mathbb P_{p_n^-}(R\le u).
\tag{7}
\]

**3. Finite saturation and symmetry.** Iterating the clipping rule along a run of ones gives exactly \(p_j^+=\min(p_+,1-b^j(1-p))\); along a run of zeros it gives \(p_j^-=\max(p_-,b^jp)\). Because \(0<b<1\), both reach their clipped endpoint after finitely many steps. Thereafter every one has probability \(p_+\), and every zero also has probability \(1-p_-=p_+\). Hence
\[
Q_n^+(p)=C_+(p)p_+^n\ (n\ge n_+(p)),\qquad
Q_n^-(p)=C_-(p)p_+^n\ (n\ge n_-(p)).
\]
The transformation \((p,X_j)\mapsto(1-p,1-X_j)\) preserves the update rule: clipping on \([\varepsilon,1-\varepsilon]\) is symmetric. Consequently the law of \(1-R\) under initial state \(p_-\) is the law of \(R\) under state \(p_+\), and
\[
\mathbb P_{p_-}(R\le u)=H_{\alpha,\varepsilon}(u).
\tag{8}
\]
Substitute these facts into (6), (7), then use (5), to obtain (1) and (2), including their endpoints by nonatomicity.

**4. Exact exponent and its optimality.** Put \(\gamma_\varepsilon=-\log_2 p_+\), so \(p_+^n=2^{-n\gamma_\varepsilon}\). If \(0<\delta<1\), write \(\delta=2^{-n}u\) with \(1/2\le u\le1\). For small \(\delta\) the integer \(n\) exceeds both saturation indices, uniformly over permitted \(p\). Also \(p_+\le H_{\alpha,\varepsilon}(u)\le1\), because the event defining \(H\) includes every sequence starting with digit one. The positive prefactors \(C_\pm(p)\) are uniformly bounded above and below on the state interval: their defining run lengths have a common finite upper bound and all cylinder factors lie in \([\varepsilon,1-\varepsilon]\). Equations (1), (2), therefore, give uniform two-sided comparability to \(\delta^{\gamma_\varepsilon}\). Finally \(\log_2 r\asymp r-1\) near \(1\) and \(1-\log_2 r\asymp2-r\) near \(2\), proving (3).

With \(u=1\), (1), (2) are exact positive multiples of \(2^{-n\gamma_\varepsilon}\). Dividing by \((2^{-n})^\beta\) diverges for every \(\beta>\gamma_\varepsilon\); the radial change of variables has a nonzero derivative at each endpoint. Thus neither endpoint has a higher pointwise Hölder exponent.

**5. Genuine discrete-scale oscillation.** For \(\alpha=1/2\), \(\varepsilon=1/4\), starting from \(p_+=3/4\), the first digit is one with probability \(3/4\). If it is zero, the next state is \(3/8\), so the probability that the first two digits are \(01\) is \((1/4)(3/8)=3/32\). Up to null dyadic sequences, \(R\ge1/4\) means that its first two digits are \(1*\) or \(01\). Hence \(H(3/4)=27/32\), whereas \(H(1)=1\). Now \(\gamma_{1/4}=\log_2(4/3)<1/2\), so
\[
(3/4)^{\gamma_{1/4}}>\sqrt{3}/2>27/32.
\]
Because (1) is exact with \(C_+(3/4)=1\), the normalized quotient along \(\delta=2^{-n}\) equals one, and along \(\delta=(3/4)2^{-n}\) equals \((27/32)/(3/4)^{\gamma_{1/4}}<1\). Formula (2) and the same symmetry give the inner-boundary assertion. This proves (4) and the failure of a single pure-power asymptotic constant.

## Verification
The proof uses only exact algebra, binary cylinder factorization and finite clipping; it is valid for all real parameters in the stated open ranges and all permitted initial states. An accompanying standard-library rational checker enumerates the binary cylinders at the test parameters \(\alpha=1/2\), \(\varepsilon=1/4\), and three initial states, comparing 36 dyadic endpoint equalities and 34 saturated nontrivial-profile equalities. It returns `CHECKS_PASS`. The finite tests are supplementary; they do not replace the universal proof.

For reproduction run `python3 check.py`. The crucial equality in the nonconstant-profile witness is \(H_{1/2,1/4}(3/4)=27/32\), independently reconstructed by the first-two-digit argument above.

## Relationship to prior work
Y. Endo, *Polynomial Random Dynamical Systems with Complete Connections and the Probability of Tending to Infinity*, arXiv:2603.20653, first posted 21 March 2026, develops the general theory of escaping probabilities. In Section 4, Example 4.2, it introduces exactly this clipped two-polynomial feedback model and proves continuity by the empty-kernel-Julia criterion; its calculation at \(r=2\) proves that the escape probability equals one. The source does not state the exact two-sided endpoint exponent, the finite-level common profile (1)–(2), or the explicit failure of a pure-power limit.

N. Arcozzi, *Dyadic potential theory and de Rham functions*, arXiv:2607.07344, studies dyadic measures arising from fixed fractional-linear functional equations and their capacitary regularity. This supplies nearby background on dyadic measure structure, but its theorems do not specify the clipped state-feedback cylinder probabilities here. K. Okamura, *On regularity for de Rham's functional equations*, arXiv:1507.05829, addresses a different class of functional equations. Familiar binary-cylinder local-dimension ideas motivate the proof, but no general result located in the sources directly states both exact feedback-dependent endpoint profiles in this model.

## Limitations
This is a theorem about the specific clipped feedback dynamics, not all random polynomial systems. It requires \(0<\alpha<1\), \(0<\varepsilon<1/2\) and gives **endpoint** regularity only, not global interior Hölder bounds or a complete multifractal spectrum. The common profile \(H_{\alpha,\varepsilon}\) is characterized probabilistically rather than by an elementary closed formula for every argument. The explicit proof of nonconstant normalized oscillations is given at \(\alpha=1/2\), \(\varepsilon=1/4\); no claim that all parameter pairs oscillate is made. Priority comparisons cannot exclude an equivalent older theorem under different measure-theoretic terminology, although the closest checked sources do not imply this exact statement.

## References
1. Y. Endo, *Polynomial Random Dynamical Systems with Complete Connections and the Probability of Tending to Infinity*, arXiv:2603.20653 (first public posting 21 March 2026), especially Section 4, Examples 4.1–4.2, and Corollary 3.9; inspected full paper, version 2.
2. N. Arcozzi, *Dyadic potential theory and de Rham functions*, arXiv:2607.07344 (8 July 2026), Sections 1–3.
3. K. Okamura, *On regularity for de Rham's functional equations*, arXiv:1507.05829 (2015/2016), related dyadic regularity background.
