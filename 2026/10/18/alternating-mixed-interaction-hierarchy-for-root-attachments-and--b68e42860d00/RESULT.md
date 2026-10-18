# Alternating mixed-interaction hierarchy for root attachments and path length in random recursive trees

## Finding

Consider a random recursive tree on the labeled vertices \(1,\ldots,n\), with each new vertex choosing a uniformly random earlier parent independently of all other choices. Write \(P_n\) for the sum of distances from the root \(1\) to all vertices and \(A_t=\mathbf1\{\text{vertex }t\text{ attaches directly to root }1\}\). For every integer \(n\ge3\), every \(1\le k\le n-2\), and every strictly increasing tuple \(3\le t_1<\cdots<t_k\le n\), set \(p_t=1/(t-1)\). Then **every mixed interaction of path length with distinct centered root-attachment decisions factorizes exactly**:
\[
\boxed{\mathbb E\!\left[P_n\prod_{i=1}^{k}(A_{t_i}-p_{t_i})\right]
=(-1)^k n\,(H_{t_1-1}-1)\prod_{i=1}^{k}\frac1{t_i(t_i-1)},\qquad H_m=\sum_{r=1}^m\frac1r.}
\tag{1}
\]
Every such mixed moment is nonzero and has sign \((-1)^k\): first-order dependence is negative, second-order dependence is positive, third-order dependence is negative, and so on at *every order and every choice of distinct arrival times*. Beyond the earliest selected time, the entire dependence on the other marked times is a product of simple reciprocal factors. This supplies the full multilinear interaction hierarchy, not merely the final covariance of total root degree with search cost.

For \(k=1\), equation (1) gives the age-resolved covariance
\[
\operatorname{Cov}(A_t,P_n)=-\frac{n(H_{t-1}-1)}{t(t-1)}.
\tag{2}
\]
The magnitude strictly decreases with \(t\ge3\). For \(k=2\), every pair of distinct nondeterministic root-attachment decisions satisfies
\[
\boxed{\operatorname{Cov}\bigl((A_s-p_s)(A_t-p_t),P_n\bigr)
=\frac{n(H_{s-1}-1)}{s(s-1)t(t-1)}>0,\qquad3\le s<t\le n.}
\tag{3}
\]
The positive second-order interaction has the opposite sign to each of the negative first-order associations. The root attachment at time \(2\) is deterministic and has no centered interaction.

## Assumptions and scope

For every \(j\in\{2,\ldots,n\}\), choose a parent \(J_j\) independently and uniformly from \(\{1,\ldots,j-1\}\). The root has depth zero, and \(P_n=\sum_{v=1}^n\operatorname{dist}(1,v)\). The indicators \(A_t=\mathbf1\{J_t=1\}\), \(t\ge3\), are independent, with probabilities \(p_t=1/(t-1)\). All expectations are with respect to this finite tree probability space. The interaction in (1) is a centered product *across distinct insertion times*, not the usual power moment of a single indicator.

## Proof

Fix the marked set of insertion times \(S=\{t_1,\ldots,t_k\}\). Conditional on the outcomes \(A_t=x_t\in\{0,1\}\) for \(t\in S\), define \(u_j(x)=\mathbb E[P_j\mid A_t=x_t\text{ for all }t\in S\text{ with }t\le j]\). Independence of parent choices gives the deterministic affine recursions, for \(j\ge3\),
\[
 u_j(x)=
 \begin{cases}
 \bigl(1+(1-x_j)/(j-2)\bigr)u_{j-1}(x)+1,&j\in S,\\
 \bigl(1+1/(j-1)\bigr)u_{j-1}(x)+1,&j\notin S.
 \end{cases}
\tag{4}
\]
Indeed, a direct root attachment gives new depth \(1\); a non-root attachment samples uniformly among vertices \(2,\ldots,j-1\), with mean parent depth \(u_{j-1}(x)/(j-2)\); an unrestricted attachment samples all earlier vertices and has mean parent depth \(u_{j-1}(x)/(j-1)\). The tree before time \(3\) has \(P_2=1\) deterministically. Thus \(u_n(x)\) is a multilinear polynomial in the marked Bernoulli outcomes.

For a multiaffine function \(f\) of independent Bernoulli variables with probabilities \(p_i\), the centered-product identity is
\[
\mathbb E\!\left[f(A)\prod_i(A_i-p_i)\right]=\left(\prod_i p_i(1-p_i)\right)\Delta_{t_1}\cdots\Delta_{t_k} f,
\tag{5}
\]
where \(\Delta_t f=f|_{x_t=1}-f|_{x_t=0}\). It follows by expanding one variable at a time, using \(\mathbb E[(A_i-p_i)f(A_i)]=p_i(1-p_i)(f(1)-f(0))\).

The unconditional path-length mean is
\[
\mathbb EP_j=j(H_j-1),
\tag{6}
\]
by summing the mean insertion depths \(\mathbb E\operatorname{dist}(1,v)=H_{v-1}\). At the first marked time \(t_1\), applying \(\Delta_{t_1}\) to (4) therefore gives
\[
\Delta_{t_1}u_{t_1}=-\frac{\mathbb EP_{t_1-1}}{t_1-2}
=-\frac{(t_1-1)(H_{t_1-1}-1)}{t_1-2}.
\tag{7}
\]
Between consecutive marked times \(t_i<t_{i+1}\), any existing nonconstant mixed-difference coefficient is multiplied by
\[
\prod_{j=t_i+1}^{t_{i+1}-1}\frac j{j-1}=\frac{t_{i+1}-1}{t_i}.
\tag{8}
\]
At the next marked time \(t_{i+1}\), its new mixed difference multiplies the existing coefficient by \(-1/(t_{i+1}-2)\), because the coefficient of \(x_{t_{i+1}}\) in the first line of (4) is exactly \(-u_{t_{i+1}-1}(x)/(t_{i+1}-2)\). After the last marked time \(t_k\), unrestricted growth multiplies the coefficient by \(n/t_k\). Combining these factors yields
\[
\Delta_{t_1}\cdots\Delta_{t_k}u_n
=(-1)^k\frac{(t_1-1)(H_{t_1-1}-1)}{t_1-2}
\left[\prod_{i=2}^k\frac{t_i-1}{t_{i-1}(t_i-2)}\right]\frac n{t_k}.
\tag{9}
\]
The bracket is the empty product \(1\) when \(k=1\). Multiplying (9) by \(\prod_i p_{t_i}(1-p_{t_i})=\prod_i(t_i-2)/(t_i-1)^2\) from (5) telescopes completely to the right-hand side of (1).

All factors after \((-1)^k\) in (1) are strictly positive since \(t_1\ge3\) implies \(H_{t_1-1}>1\), so every sign statement follows. For the extra strict monotonicity in (2), put \(b_t=(H_{t-1}-1)/(t(t-1))\). Then
\[
 b_t-b_{t+1}=\frac{2(H_{t-1}-1)-(t-1)/t}{t(t-1)(t+1)}>0,
\]
since \(H_{t-1}-1\ge1/2\) and \((t-1)/t<1\). Equation (3) is the \(k=2\) instance, whose left-hand side equals the displayed covariance because the product of two distinct centered indicators has mean zero. This proves the complete hierarchy.

## Verification

The standalone Python script `verify.py` exhaustively enumerates every legal parent sequence for \(3\le n\le8\), computes final path lengths directly, and checks equation (1) for **every nonempty subset** of nondeterministic root-attachment times, using exact rational arithmetic. In addition, exact harmonic computations check (2) and its strict age ordering through \(n=100\). Run `python verify.py` from the package directory. Finite enumeration supplements rather than proves the infinite family (1).

## Relationship to prior work

Dobrow and Fill (1999) investigated the marginal distribution, moments, and martingale limit of total path length in random recursive trees. Drmota and Hwang (2005) established joint-profile methods for final level sizes and associated aggregate path-length information. These classical works do not supply the centered multilinear interaction hierarchy over **distinct root-edge arrival times**.

More closely, Gałązka and Wdowicka (2026) give a general martingale-innovation expansion for the total path length of deterministically weighted recursive trees, including the uniform model. That stronger expansion already locates first-order search-cost fluctuations by insertion time and is relevant to (2); accordingly neither their expansion nor the standalone first-order association in (2) is claimed as the distinctive contribution. Their stated results do not provide the full arbitrary-order mixed moments between root-attachment *indicators* and path length. The extra multiaffine conditional-mean calculation in (4)--(9) establishes all-order sign alternation and the exact factorized hierarchy (1).

Another related result establishes equal contributions from every post-initial root attachment to the final **leaf count**. Its statistic is different, and it does not give the path-length interaction signs (1)--(3). The contrast between age-uniform leaf sensitivity and alternating path-length interactions motivates studying the complete hierarchy.

## Limitations

The identity concerns mixed moments under one prescribed uniform growth law. It does not assert a nontrivial causal effect under an arbitrary intervention or imply stochastic ordering of the full conditional law. It does not extend without changes to nonuniform parent weights. Although the complete hierarchy has not been found in the inspected sources, an alternative formulation via ancestral-indicator expansions or mixed derivatives of established generating functions may already exist; this is a residual originality risk. Equations (2)--(3) are stated for interpretation, with the novelty assessment concentrated on the universal arbitrary-order factorization (1).

## References

1. R. P. Dobrow and J. A. Fill, “Total Path Length for Random Recursive Trees,” *Combinatorics, Probability and Computing* 8 (1999), 317–333, DOI: 10.1017/S0963548399003855; first online publication 1999-07-01.
2. M. Drmota and H.-K. Hwang, “Profiles of random trees: correlation and width of random recursive trees and binary search trees,” *Advances in Applied Probability* 37 (2005), 321–341, DOI: 10.1239/aap/1118858628.
3. M. Gałązka and H. Wdowicka, “Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations,” arXiv:2610.00614 (2026-09-30).
4. “Equal-share covariance of root degree and leaves in a random recursive tree,” research note (2026), cited solely for the different leaf-count statistic.
