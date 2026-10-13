# Symmetry breaking in the entry flux of expiring coupon collectors

## Finding

For every integer \(n\ge2\) and window length \(M\ge n\), consider independent draws \((X_t)_{t\in\mathbb Z}\) on \([n]\) with probability vector \(p=(p_1,\ldots,p_n)\). Write \(A_t\) for the event that every type occurs in the most recent \(M\) draws, and define the stationary **new-entry flux**
\[
\mu_{n,M}(p)=\Pr(A_t\cap A_{t-1}^{c}).
\]
Unlike the stationary coverage probability \(\pi_{n,M}(p)=\Pr(A_t)\), this flux is **not** always maximized by equal sampling probabilities.

**Theorem (optimality and symmetry-breaking boundary).** On the probability simplex \(\Delta_{n-1}\), the coverage mass \(\pi_{n,M}\) has its unique maximum at \(u=(1/n,\ldots,1/n)\) for every \(M\ge n\). The flux \(\mu_{n,M}\) also has its unique maximum at \(u\) for the two shortest admissible windows \(M=n\) and \(M=n+1\). More precisely,
\[
\begin{aligned}
\mu_{n,n}(p)&=(n-1)(n-1)!\prod_{i=1}^{n}p_i,\\
\mu_{n,n+1}(p)&=\frac{n!}{2}\left(\prod_{i=1}^{n}p_i\right)\sum_{i=1}^{n}(1-p_i)^2.
\end{aligned}
\]
For two types, these are the *only* lengths for which equal probabilities maximize the flux. If \(n=2\) and \(M\ge4\), put \(k=M-1\) and let \(t_k\in(0,1)\) be the unique interior solution of
\[
1-(k+1)t+(k+1)t^k-t^{k+1}=0.
\]
The only maximizing vectors are, up to exchanging the two types,
\[
\left(\frac{t_k}{1+t_k},\frac1{1+t_k}\right).
\]
For \(M=4\), the two probabilities are \((1\pm1/\sqrt3)/2\); the maximal flux is \(1/12\), strictly larger than the uniform value \(1/16\). As \(M\to\infty\), the smaller maximizing probability is asymptotic to \(1/M\), and
\[
M\max_{p\in\Delta_1}\mu_{2,M}(p)\longrightarrow e^{-1}.
\]
For **every fixed** \(n\ge2\), equal probabilities eventually cease even to be locally optimal: \(u\) is a strict local **minimum** of the flux on \(\Delta_{n-1}\) for all sufficiently large \(M\). Moreover,
\[
\max_{p\in\Delta_{n-1}}\mu_{n,M}(p)
\ge\frac{1+o(1)}{eM},\qquad
\mu_{n,M}(u)\le\left(1-\frac1n\right)^M,
\quad M\to\infty,
\]
where \(n\) is held fixed. Thus unequal probabilities can improve the entry rate by an exponentially large factor relative to equal probabilities.

## Assumptions and scope

The draws are independent and identically distributed over a fixed finite alphabet, with one draw per time step and deterministic expiration after exactly \(M\) draws. Probability vectors may lie on the closed simplex, although any maximizer has positive coordinates. The flux is defined using a stationary two-sided sequence; a one-sided process after its initial full window has the same transition probabilities. All asymptotic statements above keep \(n\) fixed. No claim concerning the first-completion-time distribution for nonuniform draws is made.

## Proof

**1. Weighted entry identity.** Set \(L=M-1\) and let \(B_t=(X_{t-M+1},\ldots,X_{t-1})\) be the length-\(L\) overlap of the preceding and succeeding windows. A new entry with appended type \(i\) occurs exactly when (a) \(B_t\) contains every type other than \(i\) and no \(i\), (b) \(X_t=i\), and (c) the departing draw \(X_{t-M}\) differs from \(i\). The three blocks are independent. Define
\[
U_i(p,L)=\sum_{J\subseteq[n]\setminus\{i\}}
(-1)^{n-1-|J|}\left(\sum_{j\in J}p_j\right)^L.
\]
Inclusion-exclusion identifies \(U_i\) as the probability that the overlap contains every type other than \(i\), but no \(i\). Hence, for arbitrary \(p\),
\[
\boxed{\mu_{n,M}(p)=\sum_{i=1}^{n}p_i(1-p_i)U_i(p,M-1).}
\]
The factor \(1-p_i\) is essential: a departing copy of \(i\) would mean the previous window was already complete. Substituting \(p=u\) gives the known uniform formula involving Stirling numbers.

**2. Why ordinary coverage always favors uniformity.** Fix two indices \(a,b\), their sum \(s=p_a+p_b>0\), and all other coordinates. Condition on the positions occupied by types \(a,b\) and on all draws outside those positions. If those positions number \(K\), the conditional chance they include both types is
\[
1-\left(\frac{p_a}{s}\right)^K-\left(\frac{p_b}{s}\right)^K.
\]
For \(K\ge2\), this quantity is maximized by \(p_a=p_b=s/2\), strictly so when the original pair is unequal. The chance of the conditioning information is unchanged by balancing. The event that all other types occur also is unaffected. Since \(M\ge n\), a strictly positive event can realize \(K\ge2\) and cover the other types whenever every coordinate is positive. Consequently each unequal positive pair can be balanced to strictly increase \(\pi_{n,M}\). Boundary vectors have zero coverage probability, whereas \(u\) has positive coverage probability. Compactness proves unique global optimality at \(u\).

**3. Why the two shortest windows also favor uniform flux.** When \(L=n-1\), the overlap must be a permutation of the \(n-1\) other types, giving the first closed formula. When \(L=n\), the overlap has exactly one duplicated type among those \(n-1\) types. For fixed \(i\),
\[
U_i(p,n)=\frac{n!}{2}\left(\prod_{j\ne i}p_j\right)\sum_{j\ne i}p_j,
\]
which yields the second formula. At \(M=n\), arithmetic-geometric mean makes the uniform vector the unique maximizer. For \(M=n+1\), fix all coordinates except \(p_a,p_b\), retain their sum \(s\), and put \(z=p_ap_b\). Apart from a positive fixed factor, the expression to maximize is
\[
z(C-2z),\quad
C=2-2s+s^2+\sum_{j\ne a,b}(1-p_j)^2.
\]
Since \(0<z\le s^2/4\) and \(C\ge s^2\), this expression strictly increases as an unequal pair is balanced; any maximum is therefore uniform. Boundary vectors again have zero flux.

**4. Complete binary optimizer.** For \(n=2\), write \(p_1=p\), \(p_2=q=1-p\). The weighted entry identity reduces to
\[
\mu_{2,M}(p,q)=pq\bigl(p^{M-1}+q^{M-1}\bigr).
\]
At \(M=2\) this is \(pq\), and at \(M=3\) it is \(z(1-2z)\) with \(z=pq\in[0,1/4]\), uniquely maximal at \(z=1/4\). For \(M\ge4\), by symmetry take \(q\ge p\) and put \(t=p/q\in[0,1]\). Then
\[
f_k(t)=\frac{t(1+t^k)}{(1+t)^{k+2}},\qquad
\operatorname{sgn}(f_k'(t))
=\operatorname{sgn}\left(1-(k+1)t+(k+1)t^k-t^{k+1}\right).
\]
The derivative of the polynomial on the right is
\[
(k+1)\left[-1+kt^{k-1}-t^k\right].
\]
The bracket is strictly increasing on \((0,1)\), starts negative, and ends positive for \(k\ge3\). The polynomial starts at \(1\), has its sole interior minimum below zero, and ends at \(0\) with a positive derivative. Therefore it has exactly one root \(t_k\in(0,1)\), with \(f_k\) first increasing and then decreasing until \(t=1\). This proves uniqueness up to permutation. At \(M=4\), \(p^3+q^3=1-3pq\) makes \(\mu=z(1-3z)=1/12-3(z-1/6)^2\). For large \(k\), evaluating the root polynomial at \(1/(k+1)\) and \(2/(k+1)\) shows \(t_k=O(1/k)\); the root equation then implies \((k+1)t_k\to1\). Substituting into \(f_k\) gives the stated asymptotic.

**5. Local symmetry breaking for every alphabet size.** An exact curvature calculation makes the final statement quantitative. First suppose \(n\ge3\). Let \(r=n-1\), \(L=M-1\), and define the integer counts
\[
B_{r,L}=\sum_{j=0}^{r}(-1)^j\binom rj(r-j)^L,
\quad
H_{r,s}(m)=\sum_{j=0}^{s}(-1)^j\binom sj(r-j)^m.
\]
Here \(B_{r,L}=r!S(L,r)\) counts onto length-\(L\) words over \(r\) symbols, while \(H_{r,s}(m)\) counts length-\(m\) words in which \(s\) specified symbols must occur. For \(L\ge2\), put \(Q=rH_{r,r-1}(L-2)-(r-1)H_{r,r-2}(L-2)\). Directly differentiating the weighted entry identity along \(p(t)=u+t(e_1-e_2)\), fixing two positions in the overlap when taking a second derivative, gives
\[
\boxed{
 n^L[t^2]\mu_{n,M}(p(t))=
 -2B_{r,L}\left(1+\frac{(r-1)L}{r}\right)
 +rL(L-1)Q.
}
\]
The notation \([t^2]\) means the coefficient of \(t^2\) in the Taylor polynomial at zero; it is half the second derivative. For fixed \(r\ge2\) and \(L\to\infty\), inclusion-exclusion gives
\[
B_{r,L}=r^L(1+O_r(\rho^L)),\quad
Q=r^{L-2}(1+O_r(\rho^{L-2})),\quad \rho=(r-1)/r<1.
\]
Consequently
\[
[t^2]\mu_{n,M}(p(t))
=\left(\frac{r}{n}\right)^L\left(\frac{L^2}{r}+O_r(L)\right)>0
\]
for all sufficiently large \(L\). For \(r=1\), the binary calculation gives the same eventual positivity. Symmetry forces the Hessian at \(u\), restricted to the tangent space \(\{v:\sum_i v_i=0\}\), to be a scalar multiple of \(\sum_i v_i^2\); positivity on \(e_1-e_2\) makes it positive definite on this entire tangent space. As \(u\) is interior, \(u\) is eventually a strict local minimum.

**6. Quantitative separation from uniform sampling.** For fixed \(n\), choose \(p_1=1/M\) and \(p_2=\cdots=p_n=(1-1/M)/(n-1)\). The term \(i=1\) in the exact entry identity is
\[
\frac1M\left(1-\frac1M\right)^M
\Pr\bigl(\text{all remaining }n-1\text{ types appear in }M-1\text{ uniform draws}\bigr).
\]
The probability tends to one, so this single nonnegative contribution is \((1+o(1))/(eM)\). Under uniform sampling, the exact factorization from the surjection count gives
\[
\mu_{n,M}(u)=\left(1-\frac1n\right)^M
\Pr\bigl(\text{all }n-1\text{ remaining types appear in }M-1\text{ uniform draws}\bigr)
\le\left(1-\frac1n\right)^M.
\]
This completes the theorem.

## Verification

Run `python3 check_flux.py` using only the Python standard library. It enumerates exact weighted windows independently of the inclusion-exclusion flux formula, checks the two minimal-window formulas, checks the binary polynomial identity and its exact \(M=4\) certificate, and independently extracts the general Taylor coefficient in rational arithmetic. The checker is finite evidence; all infinite assertions above follow from the displayed algebraic and asymptotic arguments.

## Relationship to prior work

C. D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298 (first posted 2026-04-29), Theorem 3.1, derives the exact stationary entry flux for **uniform** draws and shows its role in rare-entry hitting-time limits. The weighted overlap identity specializes to that formula, which is not claimed as new. The theorem here concerns **optimization over the full sampling probability vector**, with an explicit two-letter bifurcation and a universal eventual local-instability result; these are not consequences of the displayed uniform formula alone. The same author's arXiv:2605.14511 concerns reset, clumsy and careless mechanisms, not this fixed-length weighted window optimization. Classical nonuniform coupon waiting-time expressions, such as C. Berthet's arXiv:1703.01886, concern monotone first collection, not stationarity-crossing flux. Existing finite-word and occupancy identities underlie the calculation but do not by themselves settle the flux optimization.

## Limitations

The flux need not directly order first-completion times, so no such comparison is asserted. A sharp first symmetry-breaking window \(M\) is determined only for \(n=2\); for larger fixed \(n\) only eventual local instability and an asymptotic global separation are established. The lower bound \((1+o(1))/(eM)\) for larger \(n\) is a constructive bound, not an asserted sharp asymptotic maximum. Earlier equivalent formulations in binary pattern-arrival theory or nonuniform scan statistics are a residual priority risk. Independent scientific validation has not been performed.

## References

1. C. D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298, version 1 posted 2026-04-29, https://arxiv.org/abs/2604.26298.
2. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511, version 1 posted 2026-05-14, https://arxiv.org/abs/2605.14511.
3. C. Berthet, *On Von Schelling Formula for the Generalized Coupon Collector Problem*, arXiv:1703.01886, posted 2017-03-06, https://arxiv.org/abs/1703.01886.
