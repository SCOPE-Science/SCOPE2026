# First non-order jump at the initial mode transition of the two-run negative binomial law

## Finding

Let \(X_{k,2}(p)\) be the number of independent Bernoulli trials with success probability \(p\in(0,1)\) until the second completed run of \(k\) consecutive successes, using the standard order-\(k\), type-I negative-binomial definition (equivalently, the sum of two independent waiting times for one such run). Put \(q=1-p\). For \(k=2,3,4\), a sharp threshold \(q_k\) exists: the unique global mode is the smallest feasible value \(2k\) for \(0<q<q_k\), while \(2k\) is not a global mode for \(q>q_k\). At the threshold there are exactly two modes, as follows:

\[
\begin{array}{c|c|c}
k & q_k & \operatorname*{arg\,max}_{m\ge 2k}\Pr(X_{k,2}(1-q_k)=m)\\\hline
2 & \sqrt{2}-1 & \{4,6\}\\
3 & (\sqrt{3}-1)/2 & \{6,9\}\\
4 & \xi\in(0.3315,0.3316) & \{8,15\}
\end{array}
\]

Here \(\xi\) is the unique root in \((3315/10000,3316/10000)\) of
\[
-2q^7+18q^5-32q^4+18q^3+6q^2-1=0.
\]
In particular, order \(k=4\) is the *first* order among \(k\ge2\) where the initial new global mode is not at offset \(k\) above the minimum: its offset is \(7\), rather than \(4\).

## Assumptions and scope

Throughout \(k\in\{2,3,4\}\), the number of required success runs is exactly two, the trials are independent with the same success probability \(0<p<1\), and modes are **global** maximizers of the probability mass function. Runs are restarted in the conventional order-\(k\), type-I waiting-time distribution. This is a theorem about three entire continuous parameter families, not a numerical sampling assertion.

The probability generating function of a single run waiting time is
\[
\mathbb E[z^{X_{k,1}}]=\frac{p^k z^k}{1-q\sum_{j=1}^{k}p^{j-1}z^j},
\]
and that of \(X_{k,2}\) is its square. Consequently define \(a_{k,n}(q)\) for \(n\ge0\) by
\[
\Pr(X_{k,2}(p)=2k+n)=p^{2k}a_{k,n}(q),\qquad a_{k,0}=1.
\]

## Proof

Logarithmic differentiation of the generating function gives the exact recurrence, valid for every integer \(n\ge1\):
\[
n a_{k,n}(q)=q\sum_{j=1}^{\min(k,n)}(n+j)(1-q)^{j-1}a_{k,n-j}(q).
\tag{1}
\]
All coefficients are nonnegative for \(0\le q\le1\). Write
\[
A_k(q)=q\sum_{j=1}^{k}(1-q)^{j-1}=1-(1-q)^k,\qquad
B_k(q)=q\sum_{j=1}^{k}j(1-q)^{j-1}.
\]
Whenever the earlier normalized masses do not exceed one, (1) gives, for \(n\ge k\),
\[
a_{k,n}(q)\le A_k(q)+B_k(q)/n.\tag{2}
\]
Strict inequality against one in (2) is propagated inductively to all later indices if its right-hand side is below one uniformly at the first tail index.

For \(k=2\), the first normalized masses are \(a_{2,1}=2q\) and \(a_{2,2}=q(q+2)\); the latter equals one precisely at \(q_2=\sqrt2-1\), while \(a_{2,1}(q_2)<1\). The functions \(A_2,B_2\) are increasing up to \(q_2\), and
\[
A_2(q_2)+B_2(q_2)/3=(-24+19\sqrt2)/3<1.
\]
Thus induction from index three proves that all higher masses are strictly below one up to and including \(q_2\). Beyond \(q_2\), \(a_{2,2}>1\).

For \(k=3\), \(a_{3,3}=2q(q+1)\) first reaches one at \(q_3=(\sqrt3-1)/2<3/8\). Each polynomial \(a_{3,n}\), \(1\le n\le5\), is strictly increasing on \((0,3/8)\), as shown by its exact Bernstein-basis derivative coefficients (reproduced by the verifier). At \(q=3/8\), the five normalized masses are
\[
3/4,\quad57/64,\quad33/32,\quad2025/2048,\quad8127/8192.
\]
Thus all indices \(n\ne3\) among the first five remain strictly below one at \(q_3\). Both \(A_3\) and \(B_3\) increase on \([0,3/8]\), and
\[
A_3(3/8)+B_3(3/8)/6=993/1024<1.
\]
Equation (2) and induction control every \(n\ge6\). Since \(a_{3,3}>1\) whenever \(q>q_3\), the threshold and both modes follow.

For \(k=4\), recurrence (1) yields
\[
\begin{aligned}
a_{4,4}(q)&=q(3q+2),\\
a_{4,7}(q)&=-2q^2(q^5-9q^3+16q^2-9q-3).
\end{aligned}
\]
Every polynomial \(a_{4,n}\) with \(1\le n\le8\) is strictly increasing on \((0,1/3)\). This statement is verified symbolically: expand each derivative in the Bernstein basis on \([0,1/3]\); every coefficient is nonnegative and at least one is positive. In particular, the Bernstein coefficients of \(a'_{4,7}\) are
\[
0,\quad2/3,\quad26/15,\quad80/27,\quad566/135,\quad16/3,\quad4630/729.
\]
Exact rational evaluation shows \(a_{4,7}(3315/10000)<1<a_{4,7}(3316/10000)\). Therefore its unique crossing \(\xi\) in that interval is the displayed polynomial root. At the upper rational endpoint, each of \(a_{4,1},\ldots,a_{4,8}\) **except** \(a_{4,7}\) is strictly less than one, so at \(q=\xi\) exactly the indices \(n=0,7\) are tied among those first nine masses.

Both \(A_4\) and \(B_4\) increase on \([0,1/3]\); for \(B'_4\) the Bernstein coefficients are \(10,50/9,25/9,29/27\). A uniform exact tail bound is
\[
A_4(1/3)+B_4(1/3)/9=716/729<1.
\]
Induction using (1) establishes \(a_{4,n}(q)<1\) for **all** \(n\ge9\) when \(0<q\le\xi\), proving that the modes at \(\xi\) are exactly \(\{8,15\}\) and that \(8\) is the unique mode below the threshold. For \(\xi<q\le1/3\), \(a_{4,7}(q)>1\); for \(q>1/3\), \(a_{4,4}(q)=q(3q+2)>1\). Thus the minimum is never a mode above \(\xi\). The two smaller orders have incoming offsets \(2\) and \(3\), proving the asserted first failure at order four.

## Verification

Run `python verify_modes.py` with Python 3 and SymPy. It regenerates the normalized probability-polynomial coefficients directly from (1), uses exact symbolic radical comparisons and rational evaluations, checks monotonicity by Bernstein coefficients, and reproduces the finite-to-infinite tail inequalities \(S_3<1\), \(S_6<1\), and \(S_9<1\) used above. A successful run prints `VERIFY_OK`. The infinite assertion is justified by (1)–(2) and induction, not by a finite computational search.

## Relationship to prior work

Georghiou, Philippou and Psillakis (2017 preprint, later expanded journal article) established mode bounds and an explicit classification at \(p=1/2\), along with selected numerical cases. Their stated results do not supply the first transition as \(p\) decreases from one for \(k=4,r=2\), nor the exact pair of initial co-modes \(\{8,15\}\) at an algebraic parameter. Shao and Wang (2017) analyze a fixed \(p=1/2\) and compute modes in particular two-success-run cases. The Poisson-of-order-\(k\) modal transition is a distinct limiting distribution and does not determine finite two-run negative-binomial modes.

## Limitations

No classification is asserted for orders \(k\ge5\), for numbers of runs other than two, or for modal transitions after the first. The findings do not preclude additional later modes as \(q\) increases. Bibliographic priority remains subject to independent full-literature verification, especially inaccessible historical articles and the later journal version of the motivating preprint.

## References

1. C. Georghiou, A. N. Philippou and Z. M. Psillakis, *A note on the modes of the negative binomial distribution of order k, type I*, arXiv:1702.02183v1, February 7, 2017; later journal article *On the modes of the negative binomial distribution of order k, type I*, DOI:10.1080/03610918.2019.1580729 (2019 online).
2. J. Shao and Q. Wang, *On the modes of some distributions of order k*, WSEAS Transactions on Mathematics 16 (2017), 216–225.
3. Y. Kwon and A. N. Philippou, *The Modes of the Poisson Distribution of Order 3 and 4*, Entropy 25 (2023), 699, DOI:10.3390/e25040699 (comparison of a different probability law).
