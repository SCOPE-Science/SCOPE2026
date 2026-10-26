# A near-square Poisson crossover for random power domination of rook graphs

## Finding

For integers \(m,n\ge 2\), let \(R_{m,n}=K_m\square K_n\) be the rook graph on cells \([m]\times[n]\). A power dominating set first observes its closed neighborhood and then repeatedly permits an observed vertex with exactly one unobserved neighbor to observe that neighbor. For \(S\subseteq[m]\times[n]\), write \(X(S)\) and \(Y(S)\) for its numbers of completely unoccupied rows and columns. The **structural criterion**, valid for every sensor set, is
\[
S\text{ power dominates }R_{m,n}\quad\Longleftrightarrow\quad X(S)\le1\ \text{or}\ Y(S)\le1.
\]
Thus the power-domination reliability is governed by two competing occupancy channels, not only by the known minimum number of sensors.

Here is the **sharp random-sensor phase diagram**. Fix a real number \(c\), and let \(m=m_n\ge n\to\infty\) be integers satisfying
\[
\frac{(m-n)\log n}{n}\longrightarrow\theta\in[0,\infty].
\]
In the independent-placement model, select each cell with probability \(p_n=(\log n+c)/m\). Equally, in the fixed-budget model, select exactly \(t_n=\lfloor n(\log n+c)\rfloor\) distinct cells uniformly at random. In **either** model, the probability that the selected set power dominates tends to
\[
\boxed{\Phi_c(\theta)=f(e^{\theta-c})+f(e^{-c})-f(e^{\theta-c})f(e^{-c}),\qquad f(u)=e^{-u}(1+u),}
\]
with the convention \(f(\infty)=0\). For finite \(\theta\), the unoccupied-row and unoccupied-column counts jointly converge to independent Poisson variables of means \(e^{\theta-c}\) and \(e^{-c}\). If \(\theta=\infty\), the unoccupied-row count diverges in probability, while the column count still converges to \(\operatorname{Pois}(e^{-c})\). In particular, a balanced board has limiting reliability \(2f(e^{-c})-f(e^{-c})^2\), whereas sufficiently asymmetric boards have limiting reliability \(f(e^{-c})\). The crossover occurs when the row excess is of order \(n/\log n\).

There is also an **exact finite reliability formula**. Set \(F_q(z)=(1+z)^q-1\), and define
\[
A_{m,n}(z)=F_n(z)^m+mF_n(z)^{m-1},
\]
\[
B_{m,n}(z)=\sum_{a=0}^1\sum_{b=0}^1\binom ma\binom nb
\sum_{i=0}^{m-a}\sum_{j=0}^{n-b}(-1)^{i+j}
\binom{m-a}{i}\binom{n-b}{j}
(1+z)^{(m-a-i)(n-b-j)}.
\]
Then the power-domination polynomial, whose coefficient of \(z^k\) counts successful sensor sets of size \(k\), is
\[
\boxed{\mathcal P(R_{m,n};z)=A_{m,n}(z)+A_{n,m}(z)-B_{m,n}(z).}
\]
Hence the exact independent-sensor success probability for \(0<p<1\) is \((1-p)^{mn}\mathcal P(R_{m,n};p/(1-p))\); the exact fixed-budget success probability is \([z^t]\mathcal P(R_{m,n};z)/\binom{mn}{t}\). As immediate finite consequences, \(\gamma_P(R_{m,n})=\min(m,n)-1\). For \(m<n\), there are \(m n^{m-1}\) minimum sensor sets; for \(m=n\), there are \(2n^n-n^2(n-1)!\).

## Assumptions and scope

Graphs are simple and undirected. Row and column indices are labeled; a sensor configuration is a set of cells, without ordering or replacement. The first observation step includes each selected cell and all cells sharing its row or column. Every later observation uses the ordinary *one remaining unobserved neighbor* rule. We assume \(m,n\ge2\). The asymptotic parameter \(n\) tends through positive integers; \(m_n\ge n\), \(c\in\mathbb R\) is fixed, and \(\theta\) may be infinite. For large enough \(n\), the displayed Bernoulli probability and the fixed budget are both admissible. The limit statements concern the stated independent-cell and uniform-fixed-size sampling models, not adversarial placement or random graphs with edges deleted.

## Proof

**1. Deterministic criterion.** Let \(r=X(S)\), \(s=Y(S)\). After the closed-neighborhood observation, exactly the \(r s\) cells in the Cartesian product of unoccupied rows and unoccupied columns remain unobserved. If \(r=0\) or \(s=0\), observation is already complete. If \(r=1\), an observed cell in an occupied row and an unoccupied column has exactly one unobserved neighbor, namely its cell in the unique unoccupied row. Such forces observe the entire remaining row; the case \(s=1\) is symmetric. If \(r,s\ge2\), each observed cell has either no unobserved neighbors, \(r\) of them, or \(s\) of them, depending on whether its row and column are occupied or not. None has exactly one, so no further force is possible. This proves the biconditional.

**2. Finite enumeration.** Configurations with at most one unoccupied row have generating polynomial \(A_{m,n}(z)\): all rows nonempty contribute \(F_n(z)^m\), and exactly one empty row contributes \(mF_n(z)^{m-1}\). The column analogue is \(A_{n,m}(z)\). Their intersection consists of arrangements with exactly \(a\) empty rows and exactly \(b\) empty columns, where \(a,b\in\{0,1\}\). Choose those empty indices, and use inclusion-exclusion to require each surviving row and column nonempty; this gives \(B_{m,n}(z)\). Union counting proves the polynomial identity. In a successful configuration at least \(m-1\) cells are needed to occupy \(m-1\) rows, or \(n-1\) are needed to occupy \(n-1\) columns. Distinct rows or columns attain these bounds. If \(m<n\), a minimum set has one cell in each of \(m-1\) chosen rows, with independent column choices, giving \(m n^{m-1}\). In the square case, both orientations contribute \(n^n\), with overlap exactly \(n^2(n-1)!\) sets having their \(n-1\) selected cells in distinct rows and distinct columns.

**3. Exact joint occupancy moments.** Let \(X_n,Y_n\) be the numbers of empty rows and columns. For any fixed nonnegative integers \(r,s\), their falling-factorial moment under independent selection is exactly
\[
\mathbb E[(X_n)_r(Y_n)_s]
=(m)_r(n)_s(1-p_n)^{nr+ms-rs},
\]
because prescribed \(r\) rows and \(s\) columns cover \(nr+ms-rs\) distinct cells. The column mean satisfies \(\mathbb EY_n=n(1-p_n)^m\to e^{-c}\). When \(\theta<\infty\), we have \(m/n\to1\) and
\[
\log\mathbb EX_n=\log m+n\log(1-p_n)
=\log(m/n)+\left(1-\frac nm\right)\log n-\frac{nc}{m}+o(1)
\longrightarrow\theta-c.
\]
The exact factorial moments therefore converge to \((e^{\theta-c})^r(e^{-c})^s\). Their limiting values are the joint factorial moments of independent Poisson variables, proving joint convergence by the multivariate factorial-moment method. Since the success event is \(\{X_n\le1\}\cup\{Y_n\le1\}\), its limiting probability is \(\Phi_c(\theta)\).

If \(\theta=\infty\), the preceding expression for \(\log\mathbb EX_n\) diverges to \(+\infty\). The empty-row indicators are independent in the Bernoulli model, so \(X_n\) is binomial with diverging mean and \(\Pr(X_n\le1)\to0\). Meanwhile \(Y_n\) converges to \(\operatorname{Pois}(e^{-c})\) by its exact factorial moments. This yields \(\Phi_c(\infty)=f(e^{-c})\).

**4. Fixed-budget sampling.** Write \(N=mn\) and \(t=t_n\). For prescribed \(r\) empty rows and \(s\) empty columns, put \(h=nr+ms-rs\). Uniform selection of exactly \(t\) cells gives the exact moment
\[
\mathbb E[(X_n)_r(Y_n)_s]
=(m)_r(n)_s\frac{\binom{N-h}{t}}{\binom Nt}.
\]
For each fixed \(r,s\), expanding \(\prod_{j=0}^{t-1}(1-h/(N-j))\) gives
\[
\log\frac{\binom{N-h}{t}}{\binom Nt}
=-\frac{t h}{N}+O\!\left(\frac{t h^2}{N^2}+\frac{t^2h}{N^2}\right)
=-\frac{tr}{m}-\frac{ts}{n}+o(1).
\]
Indeed \(m\ge n\), \(h=O(m+n)\), \(t=O(n\log n)\), so the error is \(O((\log n)^2/n)\), uniformly for fixed \(r,s\). For finite \(\theta\), these moments converge to the same product-Poisson moments as in step 3, since \(t/n=\log n+c+o(1)\). When \(\theta=\infty\), the expected number of empty rows diverges as above. For distinct rows, the fixed-budget empty-row indicators have nonpositive covariance, since the probability of avoiding two disjoint rows is no greater than the square of the probability of avoiding one. Thus \(\operatorname{Var}X_n\le\mathbb EX_n\), and Chebyshev's inequality gives \(\Pr(X_n\le1)\to0\). The column count still converges to \(\operatorname{Pois}(e^{-c})\), completing the proof of the same phase diagram.

## Verification

The included standalone `verify.py` uses direct graph-neighborhood propagation, with no assumption of the row/column criterion, to test every selected-cell subset on boards \(2\times2\), \(2\times3\), \(2\times4\), \(2\times5\), \(3\times3\), \(3\times4\), \(4\times3\), and \(4\times4\). It checks the structural condition, every coefficient of the inclusion-exclusion polynomial, and all minimum counts. An independent enumeration using exact rational arithmetic checks all mixed factorial moments of orders at most two in each coordinate, both for rectangular Bernoulli sampling and uniform fixed-size sampling. Run `python3 verify.py`; its final line is `ALL_VERIFY_OK`. These finite checks corroborate, but do not replace, the all-parameter proof.

## Relationship to prior work

Dorbec, Mollard, Klavžar, and Špacapan's 2008 paper introduced further results on power domination in graph products. Soh and Koh established the **scalar** result \(\gamma_P(K_m\square K_n)=\min(m,n)-1\) in their 2014 work on diameter-two graphs. Benson and collaborators' 2015 paper develops connections between power domination and zero forcing for graph products. Brimkov, Patel, Suriyanarayana, and Teich defined and studied the power-domination polynomial in 2018. The deterministic minimum value and the general graph-polynomial framework are not new claims. The present claim is the exact two-channel finite reliability law and its sharp **near-square** independent- and fixed-budget Poisson crossover. In accessible primary materials and targeted literature searches, no prior result covering that stochastic phase diagram was identified; this does not establish exhaustive novelty.

## Limitations

The limiting theorem assumes independent uniform cell placements or a uniformly sampled set of fixed cardinality. It does not determine reliability under correlated or optimized placements. The phase diagram concerns large boards with \(m\ge n\); interchange of the axes covers the opposite orientation. The full 2014 primary paper on diameter-two power domination could not be reviewed; an unindexed or differently worded previous result remains an originality risk. No independent validation has been performed.

## References

1. P. Dorbec, M. Mollard, S. Klavžar, S. Špacapan, *Power Domination in Product Graphs*, SIAM Journal on Discrete Mathematics 22 (2008), 554–567. DOI: 10.1137/060661879. First publicly available online 2008-03-21.
2. K. W. Soh, K. M. Koh, *A Note on Power Domination Problem in Diameter Two Graphs*, AKCE International Journal of Graphs and Combinatorics 11 (2014), 51–55. DOI: 10.1080/09728600.2014.12088762.
3. K. F. Benson et al., *Zero forcing and power domination for graph products*, arXiv:1510.02421, first version posted 2015-10-08.
4. B. Brimkov, R. Patel, V. Suriyanarayana, A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984, first version posted 2018-05-28.
