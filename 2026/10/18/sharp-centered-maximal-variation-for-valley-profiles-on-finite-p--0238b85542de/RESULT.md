# Sharp centered maximal variation for valley profiles on finite paths

## Finding

Let \(n\ge3\) and let \(f=(f_0,\ldots,f_{n-1})\) be a nonnegative **valley-shaped** sequence: for some \(p\),
\[
f_0\ge f_1\ge\cdots\ge f_p\le f_{p+1}\le\cdots\le f_{n-1}.
\]
Write \(Mf\) for the centered Hardy–Littlewood maximal function on the unweighted path with vertices \(0,\ldots,n-1\), and \(\operatorname{Var}(g)=\sum_{i=0}^{n-2}|g_{i+1}-g_i|\).

**Theorem.** The sequence \(Mf\) is valley-shaped and
\[
\operatorname{Var}(Mf)\le\left(1-\frac1n\right)\operatorname{Var}(f).
\]
The coefficient is sharp for every \(n\). Equality for a nonconstant valley-shaped input holds **if and only if** the input is a constant nonnegative baseline plus a positive spike at exactly one endpoint.

There is a quantitative two-sided endpoint rigidity estimate. With
\[
h=\min_i f_i,\quad A=f_0-h,\quad B=f_{n-1}-h,\quad
\mu=\frac1n\sum_i f_i,\quad t=\mu-h,
\]
one has \(A,B\ge0\), \(t\ge(A+B)/n\), and
\[
\operatorname{Var}(Mf)\le (A-t)_++(B-t)_+,
\qquad (u)_+=\max\{u,0\}.
\]
Consequently the sharp-coefficient deficit satisfies
\[
\boxed{\left(1-\frac1n\right)\operatorname{Var}(f)-\operatorname{Var}(Mf)
\ge\frac{\min\{(n-1)A,B\}+\min\{(n-1)B,A\}}{n}.}
\]
The displayed endpoint-mass deficit is sharp: equality holds for every \(n\) on profiles \(f=(h+a,h,\ldots,h,h+a)\), where \(h\ge0\) and \(a>0\). In particular a genuine trough with both endpoint excesses positive has strictly positive deficit.

## Assumptions and scope

The vertex measure is counting measure; every graph ball is the closed integer-radius ball truncated at the two path endpoints. Explicitly,
\[
(Mf)_i=\max_{0\le r\le n-1}
\frac{\sum_{j=\max(0,i-r)}^{\min(n-1,i+r)}f_j}
{\min(n-1,i+r)-\max(0,i-r)+1}.
\]
All comparisons are exact and include plateaus at the trough or endpoints. The results also apply to a real or complex input whose **modulus** is valley-shaped, since the graph maximal function depends only on that modulus; the variation in the conclusion is then that of the modulus.

## Proof

**1. Shape preservation for complete sliding windows.** Suppose \(f\) has a trough at \(p\). For each fixed radius \(r\), define on the valid-center interval \(r\le x\le n-1-r\)
\[
T_r(x)=\frac1{2r+1}\sum_{j=x-r}^{x+r}f_j.
\]
For adjacent valid centers,
\[
(2r+1)(T_r(x+1)-T_r(x))=f_{x+r+1}-f_{x-r}.
\]
The sign on the right can change from negative to positive but not from positive to negative as \(x\) increases. Indeed, if both indices are at or before the trough, the difference is nonpositive; if both are at or after it, the difference is nonnegative. In the intervening regime the left sampled value is nonincreasing and the right sampled value nondecreasing, so their difference is nondecreasing. Hence every \(T_r\) is valley-shaped on its valid domain, including possible equality plateaus.

**2. Shape preservation after endpoint truncation.** We verify the global quasiconvex inequality
\[
(Mf)_j\le\max\{(Mf)_i,(Mf)_k\}\qquad(0\le i<j<k\le n-1).
\]
Fix any ball centered at \(j\). If it meets both endpoints, its average is the global mean \(\mu\), attainable from either comparison center. If the ball is clipped only at the left endpoint, write it as \([0,b]\). Its radius about \(j\) is at least \(j\), so \(b\ge2j\). The same interval \([0,b]\) is a centered graph ball about the earlier vertex \(i\), using radius \(b-i\). Thus its average is at most \((Mf)_i\). Right-clipped balls are handled symmetrically using \(k\).

For an untruncated ball of radius \(r\), its average equals \(T_r(j)\). Put \(i'=\max\{i,r\}\) and \(k'=\min\{k,n-1-r\}\), so \(i'\le j\le k'\). Valley shape of \(T_r\) gives \(T_r(j)\le\max\{T_r(i'),T_r(k')\}\). If \(i'=i\), the first term is an admissible ball average at \(i\); if \(i'=r>i\), then \(T_r(r)\), the mean on \([0,2r]\), is still a centered ball average at \(i\), using radius \(2r-i\). The corresponding assertion for \(k'\) follows by reflection. Therefore the given ball average at \(j\) is no larger than \(\max\{(Mf)_i,(Mf)_k\}\). Maximizing over all radii proves the inequality. On a finite ordered set it is equivalent to valley shape of \(Mf\).

**3. Endpoint values.** Let \(P_s=(s+1)^{-1}\sum_{j=0}^{s}f_j\). If \(P_s>P_{s-1}\), then \(f_s>P_{s-1}\), which can occur only on the nondecreasing side of the trough. Since \(f_{s+1}\ge f_s>P_s\), every subsequent prefix-mean increment is also positive. Thus the prefix means first decrease (weakly) and then increase (weakly), attaining their maximum at the initial or full-length prefix. This gives
\[
(Mf)_0=\max\{f_0,\mu\}.
\]
The identical suffix argument gives \((Mf)_{n-1}=\max\{f_{n-1},\mu\}\). Every center admits the entire path as one ball, so \(\min_i(Mf)_i\ge\mu\).

**4. Variation and quantitative deficit.** Because \(Mf\) is valley-shaped,
\[
\operatorname{Var}(Mf)=(Mf)_0+(Mf)_{n-1}-2\min_i(Mf)_i.
\]
The endpoint formulas imply the claimed bound \((A-t)_++(B-t)_+\). Furthermore \(\operatorname{Var}(f)=A+B\). All interior terms of \(f-h\) are nonnegative, hence \(t\ge(A+B)/n\). Therefore
\[
\begin{aligned}
\left(1-\frac1n\right)(A+B)-\operatorname{Var}(Mf)
&\ge\left(1-\frac1n\right)(A+B)
-\left(A-\frac{A+B}{n}\right)_+
-\left(B-\frac{A+B}{n}\right)_+\\
&=\frac{\min\{(n-1)A,B\}+\min\{(n-1)B,A\}}n.
\end{aligned}
\]
This is nonnegative and strictly positive whenever \(A,B>0\).

**5. Equality and sharpness.** For nonconstant inputs, equality in the coefficient bound forces at least one of \(A,B\) to vanish by the positive-gap estimate. Suppose \(B=0\) and \(A>0\). Equality forces \(t=A/n\), since \((A-t)_+\le A-t\) for \(t\le A\), with strict deficit for \(t>A/n\). As \(t=(A+\sum_{i=1}^{n-2}(f_i-h))/n\), all interior entries equal \(h\). Thus \(f\) is an endpoint spike on a constant baseline; reflection covers \(A=0\). Conversely, for such an endpoint spike of height \(a>0\), the maximal function decreases from \(h+a\) to the global mean \(h+a/n\), yielding exactly \(\operatorname{Var}(Mf)=a(1-1/n)\).

For the two-equal-endpoint-spike profile \(f=(h+a,h,\ldots,h,h+a)\), the maximal function has endpoint values \(h+a\), and a central vertex with maximal value exactly the full-path mean \(h+2a/n\). For odd \(n\), the middle vertex has no one-endpoint-only centered ball; for even \(n\), at either middle vertex such a ball has at least \(n-1\) sites and mean at most \(h+a/(n-1)\le h+2a/n\). Hence \(\operatorname{Var}(Mf)=2a(1-2/n)\), and the quantitative deficit equals \(2a/n\), exactly the right side of the boxed inequality.

## Verification

The standalone standard-library script `verify.py` uses `fractions.Fraction` throughout its tested domain. It checks the graph-ball formula, valley preservation, the exact endpoint identities, the sharp inequality, the quantitative gap, the equality classification, and endpoint-spike sharpness for every integer-valued valley profile with values in \(\{0,1,2,3\}\) and lengths \(3\) through \(10\): \(13{,}652\) profiles, including \(13{,}620\) nonconstant profiles. Four supplementary rational profiles are also checked. Exact calculations corroborate, but do not replace, the proof for arbitrary real amplitudes and arbitrary path length.

## Relationship to prior work

González-Riquelme, Kovač, and Madrid [1] formulate the unrestricted finite-path sharp-variation conjecture and prove the coefficient for paths on four vertices, with additional numerical small-graph evidence. The present result resolves the entire all-length **single-trough class**, not the unrestricted conjecture.

Earlier one-dimensional centered-maximal variation theorems for indicator functions and special attachment conditions [2] concern functions on the infinite line and do not provide the finite-path sharp coefficient or this endpoint-mass rigidity. Ramos [3] studies centered/nontangential maximal variation and valley structure on detachment intervals, not the finite-path assertion for all nonnegative single-trough inputs. Existing monotone-input and single-peak-input cases do not contain genuinely two-sided troughs such as \((1,0,\ldots,0,1)\).

## Limitations

The theorem assumes one trough (equivalently, one interval of minima) in the modulus profile. It does not settle the unrestricted sharp path conjecture and does not claim a bound for arbitrary oscillatory inputs. The rigorous proof supplies no classification of the location of the trough of \(Mf\), only its existence. The asserted originality is relative to the explicitly compared accessible literature; older or less-indexed results may contain equivalent observations. No independent mathematical validation is represented.

## References

[1] C. González-Riquelme, V. Kovač, and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1 (first public version 12 March 2026), especially Conjecture 5 and Sections 3–4. https://arxiv.org/pdf/2603.12462

[2] C. Bilz and J. Weigt, *The one-dimensional centred maximal function diminishes the variation of indicator functions*, Journal of Geometric Analysis **35** (2025), article 256; arXiv:2107.12404, especially Theorems 1.3 and 1.5. https://arxiv.org/pdf/2107.12404

[3] J. P. G. Ramos, *Sharp total variation results for maximal functions*, Annales Academiae Scientiarum Fennicae Mathematica **44** (2019), 41–64, especially the detachment-interval valley lemma. https://www.acadsci.fi/mathematica/Vol44/vol44pp0041-0064.pdf
