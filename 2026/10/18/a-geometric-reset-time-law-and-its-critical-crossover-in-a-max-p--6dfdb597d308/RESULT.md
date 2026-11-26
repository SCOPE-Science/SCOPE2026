# Complete-reset statistics and quantitative small-coupling stability in a max-plus four-cycle

## Finding

For the generalized max-plus map of Ohmori and Yamazaki [1],
\[
F_{T,D,B}(X,Y)=\bigl(Y+T\max(X,0),\ B-D\max(X,0)\bigr),
\]
fix \(B>0\), \(D>1\) and \(T\ge0\) with \(D>1+T+T^2\). This is exactly the parameter region used in [1, Eq. (5)] for the stable period-four itinerary. Given an initial state \((X,Y)\), define
\[
x_0=X,\quad x_1=Y+T\max(X,0),\quad
x_{n+2}=B+T\max(x_{n+1},0)-D\max(x_n,0).
\]
The *first complete-reset time* is
\[
R_T=2+\inf\{j\ge0:x_j\le0\ \text{and}\ x_{j+1}\le0\};
\]
by convention \(R_T=\infty\) if the set is empty. Such an event sends the planar orbit to the specific state \((B,B)\) at time \(R_T\). It may not be the first arrival at *some* phase of the stable cycle.

Let the initial pair be sampled uniformly from the natural invariant square of the decoupled boundary map,
\[
I_D^2,\qquad I_D=[B(1-D),B].
\]
For \(h,k\in\{1,2,\ldots\}\), define
\[
\mathcal R(h,k)=
\begin{cases}
 2\max(h,k),&h\equiv k\pmod 2,\\
 2h-1,&h>k\ \text{and}\ h\not\equiv k\pmod2,\\
 2k+1,&k>h\ \text{and}\ h\not\equiv k\pmod2.
\end{cases}
\]
If \(H_1,H_2\) are independent with
\[
\Pr(H_i=h)=(1-D^{-1})D^{-(h-1)},\quad h\ge1,
\]
then the complete limiting law is **exactly**
\[
R_0\ \overset{\mathrm d}=\ \mathcal R(H_1,H_2),\qquad
\mathbb E R_0=\frac{2D(D+2)}{D^2-1}.
\]
Moreover, at each fixed \(D>1\) and \(B>0\),
\[
\big\|\mathcal L(R_T)-\mathcal L(R_0)\big\|_{\mathrm{TV}}
=O_D\big(T\log(1/T)\big)\qquad(T\downarrow0),
\]
where the possible value \(\infty\) is included in the underlying countable state space. In the separate critical limit \(D\downarrow1\) at \(T=0\),
\[
(D-1)R_0\ \Longrightarrow\ 2\max(E_1,E_2),\quad
\Pr\big(2\max(E_1,E_2)\le t\big)=(1-e^{-t/2})^2\quad(t\ge0),
\]
with independent unit-exponential \(E_i\), and \((D-1)\mathbb E R_0\to3\).

## Assumptions and scope

The scalar recurrence is defined for all real initial coordinates. The probabilistic laws refer only to normalized Lebesgue area on \(I_D^2\), a dynamically distinguished square invariant for the boundary model \(T=0\). The square is **not** asserted invariant for \(T>0\). Equalities at switch thresholds are allowed in the definition of \(R_T\); all exceptional points lying on a finite switch preimage have probability zero. The perturbative limit fixes \(D\) and \(B\) before letting \(T\to0\). The critical \(D\to1\) statement applies to the separate boundary model \(T=0\).

## Proof

**1. Four-cycle and reset.** The planar map takes \((B,B)\) successively through
\[
\begin{split}
P_0&=(B,B),\\
P_1&=(B(1+T),\ B(1-D)),\\
P_2&=(B(1+T+T^2-D),\ B(1-D(1+T))),\\
P_3&=(B(1-D(1+T)),\ B).
\end{split}
\]
The strict inequality \(D>1+T+T^2\) makes both entries of \(P_2\) negative and gives \(F(P_3)=P_0\), so these are four distinct phases. If \(x_j,x_{j+1}\le0\), the recurrence gives \(x_{j+2}=B\) and \(x_{j+3}=B(1+T)\). The planar state at time \(j+2\) is \((B,B)\), since the second coordinate is \(B-D\max(x_{j+1},0)=B\). This proves the deterministic meaning of a complete reset.

**2. One-dimensional decoupling and geometric first reset.** Put \(g_D(z)=B-D\max(z,0)\). At \(T=0\) the scalar recurrence decouples:
\[
x_{2k}=g_D^k(X),\qquad x_{2k+1}=g_D^k(Y).
\]
The interval \(I_D\) is mapped into itself. For \(z\in I_D\), define \(H(z)=\inf\{h\ge1:g_D^h(z)=B\}\). Apart from the countable set of preimages of the repelling fixed point \(B/(D+1)\) and switch thresholds, this is finite. For every \(n\ge1\), the event \(H(z)>n\) is exactly that the first \(n\) values \(g_D^0(z),\ldots,g_D^{n-1}(z)\) are positive, up to null boundary points. The surviving cylinder \(S_1=(0,B)\) has length \(B\); inductively \(S_{n+1}=g_D^{-1}(S_n)\cap(0,B)\), and the affine branch of \(g_D\) maps \((0,B)\) bijectively onto the interior of \(I_D\) with slope \(-D\). Therefore \(|S_n|=B/D^{n-1}\), and division by \(|I_D|=BD\) yields
\[
\Pr(H>n)=D^{-n},\qquad
\Pr(H=h)=(1-D^{-1})D^{-(h-1)}.
\]
The two coordinate variables are independent by the product sampling rule.

**3. Exact parity-dependent reset law.** If \(H(z)=h<\infty\), the scalar values \(g_D^k(z)\) are positive for \(0\le k\le h-2\), nonpositive at \(k=h-1\), and subsequently alternate between \(B\) and \(B(1-D)<0\). Thus their nonpositive indices are exactly \(h-1,h+1,h+3,\ldots\). With the even and odd subsequences in step 2, a pair of consecutive nonpositive scalar values begins at an even time when \(H(X)\) and \(H(Y)\) have the same parity; the first such time is \(2(\max(H(X),H(Y))-1)\). When the parities differ, the first pair begins at the odd time \(2H(X)-3\) if \(H(X)>H(Y)\), and \(2H(Y)-1\) if \(H(Y)>H(X)\). Adding two steps proves \(R_0=\mathcal R(H(X),H(Y))\) almost surely, hence the exact full discrete law.

**4. Mean and critical law.** Write \(M=\max(H_1,H_2)\). Since the independent variables are identically distributed, interchanging their labels makes the odd-parity \(-1\) and \(+1\) corrections cancel in expectation. Consequently \(\mathbb E R_0=2\mathbb E M\), and the tail-sum formula gives
\[
\mathbb E M=\sum_{k=0}^{\infty}(2D^{-k}-D^{-2k})
=\frac{D(D+2)}{D^2-1}.
\]
As \(D\downarrow1\), geometric survival yields \((D-1)H_i\Rightarrow E_i\), where \(E_i\) is exponential of mean one. The deterministic bound \(|R_0-2M|\le1\), the continuous mapping theorem, and Slutsky's lemma yield the stated critical limiting law. The mean asymptotic follows directly from the exact rational formula.

**5. Quantitative total-variation stability.** Dividing all state coordinates by \(B\) leaves reset times unchanged, so set \(B=1\). Couple the two orbits at the same random initial point. Set \(M_0=\max(1,D-1)\), \(d=\min(1,D-1)>0\), \(a=\sqrt D>1\), and \(e_j=|x_j(T)-x_j(0)|\). The boundary orbit has absolute values at most \(M_0\), so \(e_0=0\), \(e_1\le T\), and
\[
e_{j+2}\le D e_j+T e_{j+1}+TM_0.
\]
With \(c=M_0/(D-1)\), the comparison sequence \(f_j=e_j+cT\) satisfies \(f_{j+2}\le D f_j+T f_{j+1}\). Since \((a+T)^2\ge D+T(a+T)\), it follows by induction that \(e_j\le (1+c)T(a+T)^j\).

At \(T=0\), the marginal of \(x_j(0)\) is a uniform measure on \(I_D\) of weight \(D^{-\lfloor j/2\rfloor}\), plus atoms supported on \(\{1,1-D\}\). This follows by iterating the scalar map: one application transfers a fraction \(1/D\) of its uniform component back to a uniform distribution on the same interval, with the remainder sent to \(1\); the two atoms map to each other. Hence for \(0\le u<d\),
\[
\Pr(|x_j(0)|\le u)\le (2u/D)D^{-\lfloor j/2\rfloor}.
\]
Choose an integer \(K\) depending only on \(D\), large enough that \(2(1+c)a^{-K}<d\), and let \(N=\lfloor\log(1/T)/\log a\rfloor-K\). For small enough \(T>0\), \((1+T/a)^N\le2\) and \(N\ge2\). For every \(j\le N\), the deterministic error bound lies below \(d\), and the probability that the Boolean switch \(x_j\le0\) differs between the two orbits is at most
\[
\frac{2(1+c)}D T(a+T)^j D^{-\lfloor j/2\rfloor}\le \frac{4a(1+c)}D T.
\]
If \(R_0\le N\) and all these switches agree, the reset times are equal. The geometric law and \(R_0\le2\max(H_1,H_2)+1\) give \(\Pr(R_0>N)\le 2D^{-\lfloor(N-1)/2\rfloor}=O_D(T)\). Adding the switch-error bound over \(0\le j\le N\) and using the coupling inequality
\[
\|\mathcal L(R_T)-\mathcal L(R_0)\|_{\mathrm{TV}}
\le\Pr(R_T\ne R_0),
\]
proves the claimed rate, including the possible symbol \(\infty\).

## Verification

The bundled standard-library script `check_capture.py` checks the four exact cycle phases, the complete parity formula against independently iterated rational orbits at five values of \(D\), and finite rational partial sums against the closed expected value. The script returns `EXACT_RESET_CYCLE_AND_GEOMETRIC_MOMENT_CHECK_OK 1600`. It does not infer any infinite-time theorem from finite tests. Reproduce with `python3 check_capture.py`.

## Relationship to prior work

Ohmori–Yamazaki [1], Sections 2–5, supply the map, reset mechanism, regime \(D>1+T+T^2\), and four phases. Their prior [2], Section 3, gives the cycles and Poincaré map at \(T=0\). A separate [November 8, 2026 capture-time analysis](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-exact-original-time-capture-statistics-and-critical-scaling-in-a--4b0c6f578196/RESULT.md) treats the same scalar decoupling, independent geometric times, and maximum-of-exponentials limit. It samples \((0,B)^2\), which two planar iterations send uniformly onto \(I_D^2\), and stops at the first arrival to any attracting phase. For samples started in \((0,B)^2\), this arrival and arrival to \((B,B)\) differ by a delay of zero to three iterations, almost surely. Thus the common critical limit is not a distinct result here. The exact finite-\(D\) parity corrections and mean given here specify the complete-reset clock; the quantitative perturbative estimate concerns that clock with \(T>0\), not capture onto the unperturbed cycle.

## Limitations

A complete reset time is not interchangeable with first arrival at any of the four phase points. The result gives no universal bound on \(R_T\), no convergence of \(\mathbb E R_T\) as \(T\to0\), and no simultaneous scaling limit in \(T\) and \(D-1\). The exceptional measure-zero initial points are excluded only from the probability statements; they may exhibit other behavior. Neither a uniqueness claim among all literature nor independent mathematical verification is asserted.

## References

[1] S. Ohmori and Y. Yamazaki, “A Generalization for Ultradiscrete Limit Cycles in a Certain Type of Max-Plus Dynamical Systems,” arXiv:2402.06230v1 (first public 9 February 2024); *Journal of Mathematical Physics* **65**, 082705 (2024), doi:10.1063/5.0203186. Source: https://arxiv.org/html/2402.06230v1.

[2] S. Ohmori and Y. Yamazaki, “Dynamical properties of discrete negative feedback models,” arXiv:2305.05908v1 (10 May 2023). Source: https://arxiv.org/html/2305.05908v1.
