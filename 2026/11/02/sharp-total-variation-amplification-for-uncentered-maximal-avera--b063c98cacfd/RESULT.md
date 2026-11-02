# Sharp total variation amplification for uncentered maximal averages on finite star graphs

## Finding

For each integer \(k\ge1\), let \(S_{k+1}\) be the unit-edge star with one hub and \(k\) leaves. On vertex functions with counting measure define the **uncentered graph-ball maximal operator** \(\widetilde M\): at a vertex \(v\), take the largest average of \(|f|\) over all metric balls, *with arbitrary center*, that contain \(v\). Then the exact, attained \(1\)-variation operator constant is
\[
\boxed{\sup_{\operatorname{Var}(f)>0}\frac{\operatorname{Var}(\widetilde M f)}{\operatorname{Var}(f)}=C_k=\frac{k^2-k+2}{2(k+1)}.}
\]
For every \(k\), an indicator function of a single leaf attains this ratio. It is strictly below one for \(k=1,2\), equals one at \(k=3\), and is strictly greater than one for every \(k\ge4\). Moreover \(C_k=k/2-1+2/(k+1)\), so amplification grows linearly with branching.

## Assumptions and scope

The graph \(S_{k+1}\) has vertices \(\{c,v_1,\ldots,v_k\}\), edges \(\{\{c,v_i\}:1\le i\le k\}\), unit-edge shortest-path metric \(d\), and counting measure. For \(x\in V\) and \(r\ge0\), set \(B(x,r)=\{u:d(x,u)\le r\}\). All radii are allowed; repeated balls are immaterial. For every real-valued vertex function \(f\),
\[
(\widetilde M f)(v)=\max_{\substack{x\in V,\ r\ge0\\v\in B(x,r)}}\frac{1}{|B(x,r)|}\sum_{u\in B(x,r)}|f(u)|,
\quad
\operatorname{Var}(f)=\sum_{i=1}^{k}|f(v_i)-f(c)|.
\]
The supremum is over nonconstant real-valued \(f\). No assumption of nonnegativity or symmetry is made. The centering freedom in the operator is essential: this is not the centered maximal operator.

## Proof

**Complete enumeration of relevant balls.** Balls containing the hub \(c\) are precisely \(\{c\}\), \(\{c,v_j\}\) for \(1\le j\le k\), and \(V\). Balls containing a fixed leaf \(v_i\) are precisely \(\{v_i\}\), \(\{c,v_i\}\), and \(V\). This also applies when \(k=1\), with harmless duplicate sets.

Put \(g=|f|\), \(b=g(c)\), and \(t_i=g(v_i)-b\), so \(\operatorname{Var}(g)=\sum_i|t_i|\le\operatorname{Var}(f)\). The nonnegative function \(g\) permits removal of the common baseline \(b\) from every ball average. Write
\[
q=\max_{1\le i\le k}t_i,\qquad s=\frac{\sum_{i=1}^{k}t_i}{k+1},\qquad H=\max\{0,q/2,s\},\qquad L_i=\max\{t_i,t_i/2,s\}.
\]
By the ball enumeration, \((\widetilde Mf)(c)=b+H\) and \((\widetilde Mf)(v_i)=b+L_i\). Thus \(\operatorname{Var}(\widetilde Mf)=\sum_i|L_i-H|\).

**Sharp coordinatewise bound.** Define \(\alpha_k=(k-1)/(2(k+1))\). For every \(i\),
\[
|L_i-H|\le \frac12|t_i|+\alpha_k\sum_{j\ne i}|t_j|.\tag{1}
\]
We establish it without sign restrictions on the \(t_i\). First suppose \(L_i\ge H\). Because \(H\ge\max\{0,t_i/2,s\}\), a strict positive excess can only come from the choice \(L_i=t_i\ge0\), and then \(0\le L_i-H\le t_i/2\). If \(H>L_i\) and \(H=0\), necessarily \(t_i<0\) and \(L_i\ge t_i/2\), giving \(H-L_i\le |t_i|/2\).

It remains to handle \(H>L_i\) with \(H>0\). The maximizing term in \(H\) cannot be \(s\), because \(L_i\ge s\). Hence \(H=q/2>0\). An index \(j\) attaining \(q\) must satisfy \(j\ne i\): otherwise \(L_i\ge t_i=q\ge q/2=H\), a contradiction. Consequently \(k\ge2\), and, using \(L_i\ge s\),
\[
\begin{aligned}
H-L_i&\le q/2-s\\
&=\frac{k-1}{2(k+1)}t_j-\frac{t_i}{k+1}-\frac{1}{k+1}\sum_{\ell\notin\{i,j\}}t_\ell\\
&\le \frac12|t_i|+\alpha_k\sum_{\ell\ne i}|t_\ell|.
\end{aligned}
\]
Here \(t_j=q>0\), \(1/(k+1)\le1/2\), and \(\alpha_k\ge1/(k+1)\) when \(k\ge3\); when \(k=2\) the final sum over \(\ell\notin\{i,j\}\) is empty. This proves (1) also for \(k=1\), when the last case is impossible.

**Global inequality.** Sum (1) over the \(k\) leaves:
\[
\operatorname{Var}(\widetilde Mf)\le\left(\frac12+(k-1)\alpha_k\right)\sum_i|t_i|=\frac{k^2-k+2}{2(k+1)}\operatorname{Var}(g)\le C_k\operatorname{Var}(f).
\]

**Sharpness.** Choose \(f=\mathbf1_{\{v_1\}}\). Then \(\operatorname{Var}(f)=1\); the hub maximal value is \(1/2\), the marked leaf maximal value is \(1\), and each other leaf has maximal value \(1/(k+1)\). Hence
\[
\operatorname{Var}(\widetilde Mf)=\frac12+(k-1)\left(\frac12-\frac{1}{k+1}\right)=C_k,
\]
including \(k=1\). Finally \(C_k-1=k(k-3)/(2(k+1))\), proving the exact threshold; \(C_{k+1}-C_k=1/2-2/[(k+1)(k+2)]>0\) for every \(k\ge1\). This completes the proof for **every** integer \(k\ge1\).

## Verification

The standalone `verify_star_uncentered.py` uses exact integer or rational arithmetic and independently enumerates all metric graph balls. It checked \(488{,}280\) normalized configurations with \(t_i\in\{-2,-1,0,1,2\}\) for \(1\le k\le8\), \(3{,}276\) independent direct ball-average evaluations, the leaf-indicator extremizer in each of those eight dimensions, and another hundred rational extremizer identities for \(1\le k\le100\). All tests passed. To reproduce, run `python verify_star_uncentered.py` with Python 3. The finite tests are supplementary: the unrestricted theorem is proved by the preceding inequalities and exact witness.

## Relationship to prior work

Bober, Carneiro, Hughes, and Pierce proved that the **uncentered discrete interval** maximal operator contracts total variation on the whole integer line (arXiv:1005.3030, Theorem 1). Graphs with branching are not covered by that one-dimensional result; the present sharp star constants grow without bound. Soria and Tradacete studied graph-ball maximal operators and their bounds (arXiv:1410.6204). González-Riquelme and Madrid determined sharp **centered** graph maximal-function variation constants on stars, including the \(1\)-variation constant \(k/(k+1)\) (arXiv:2005.03146). That centered result does not imply the uncentered constant: their difference here is \((k-1)(k-2)/(2(k+1))\), strictly positive for \(k\ge3\). Their sequel (arXiv:2011.02630) addresses further centered maximal inequalities. Later finite-graph results on centered variation (arXiv:2603.12462) likewise concern a different operator.

The 2021 finite-graph variation paper by Liu and Xue (DOI 10.1007/s13348-020-00290-6) is relevant, but its full text was not available for this comparison; a possible earlier equivalent uncentered result cannot be categorically excluded. No uniqueness or publication-priority claim is made.

## Limitations

The theorem is restricted to unweighted stars with the standard **uncentered graph-ball** averaging family and unweighted total edge variation. It does not assert a sharp formula for arbitrary trees, weighted vertex measures, connected induced-set averages (which are a different operator), or higher \(p\)-variation exponents. The external literature comparison does not substitute for independent expert priority review.

## References

1. J. Bober, E. Carneiro, K. Hughes, L. B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030, first posted 2010-05-17. https://arxiv.org/abs/1005.3030
2. J. Soria, P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204, first posted 2014-10-22. https://arxiv.org/abs/1410.6204
3. C. González-Riquelme, J. Madrid, *Sharp Inequalities for maximal operators on finite graphs*, arXiv:2005.03146, first posted 2020-05-06. https://arxiv.org/abs/2005.03146
4. C. González-Riquelme, J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630. https://arxiv.org/abs/2011.02630
5. F. Liu, Q. Xue, *On the variation of the Hardy–Littlewood maximal functions on finite graphs*, Collectanea Mathematica 72 (2021), 333–349. https://doi.org/10.1007/s13348-020-00290-6
6. C. González-Riquelme, I. Kovač, J. Madrid, finite-graph centered maximal variation study, arXiv:2603.12462. https://arxiv.org/abs/2603.12462
