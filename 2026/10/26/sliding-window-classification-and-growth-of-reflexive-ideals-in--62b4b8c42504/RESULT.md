# Sliding-window classification and growth of reflexive ideals in terminal-gap numerical semigroups

## Finding
For integers \(r\ge3\) and \(m\ge r+1\), consider the numerical semigroup
\[
S_{m,r}=\{0\}\cup [m,2m-r-1]\cup[2m,\infty)\cap\mathbb Z,
\]
where intervals throughout are integer intervals. Put \(L=m-r\). A length-\(L\) binary word is **admissible** when every maximal run of ones strictly inside the word has length at least \(r\); runs touching an endpoint are unrestricted. For \(Z\subseteq\{0,\ldots,L-1\}\), define the windows and completion set
\[
E_x=\{i\in[0,L-1]:2m-r\le m+i+x\le2m-1\}
     =[L-x,L+r-1-x]\cap[0,L-1],\quad 1\le x<m,
\]
\[
U_Z=\{x\in[1,m-1]:E_x\subseteq Z\}.
\]
The complete set of normalized reflexive relative ideals (those with minimum zero and \(I=S_{m,r}-(S_{m,r}-I)\)) consists of \(S_{m,r}\) together with the **pairwise distinct** ideals
\[
I_Z=S_{m,r}\cup[2m-r,2m-1]\cup U_Z,
\]
one for each admissible word, where \(Z\) is its set of one-positions. For the nontrivial ideals, inclusion is exactly inclusion of the one-position sets: \(I_Z\subseteq I_W\) if and only if \(Z\subseteq W\). Thus their joins correspond to union of word supports. In particular, if \(a_r(L)\) denotes the number of admissible words, the exact number of normalized reflexive ideals is \(1+a_r(m-r)\), and
\[
\sum_{L\ge0}a_r(L)z^L
 =\frac1{1-z}+\frac{z}{(1-z)((1-z)^2-z^{r+1})}.
\]
For every fixed \(r\ge3\), this number grows exponentially with \(L=m-r\). There is a unique \(\rho_r\in(0,1)\) satisfying
\[(1-\rho_r)^2=\rho_r^{r+1},\]
and
\[
a_r(L)\sim
\frac{\rho_r^{-L}}{(1-\rho_r)(2(1-\rho_r)+(r+1)\rho_r^r)}.
\]
The growth constants \(\rho_r^{-1}\) decrease strictly to \(1\) as \(r\to\infty\). For the first new block length \(r=3\), the constant is the golden ratio \((1+\sqrt5)/2\).

## Assumptions and scope
We use \(\mathbb N_0=\{0,1,2,\ldots\}\) and \([a,b]=\{j\in\mathbb Z:a\le j\le b\}\). The addition closure of \(S_{m,r}\) follows because its positive members are all at least \(m\), so the sum of two positive members is at least \(2m\). Its conductor is \(2m\) and its Frobenius number is \(2m-1\).

A relative ideal of a numerical semigroup \(S\) is a nonempty subset \(I\subseteq\mathbb Z\) with a minimum and \(I+S=I\). Its ideal quotient is \(S-I=\{t\in\mathbb Z:t+I\subseteq S\}\); its divisorial or reflexive closure is \(I^v=S-(S-I)\). An ideal is normalized if its minimum is \(0\), hence it contains \(S\) and is contained in \(\mathbb N_0\). All counts are counts of normalized ideals, equivalently of translation classes of relative ideals. The claim concerns \(r\ge3\), not the previously treated \(r=2\) case.

## Proof
**1. The quotient has a sliding-window normal form.** Write \(P=[m,2m-r-1]\), \(B=[2m-r,2m-1]\), and let \(I\ne S=S_{m,r}\) be a normalized relative ideal. Its gap additions split uniquely as \(U=I\cap[1,m-1]\) and \(V=I\cap B\). Since \(0\in I\), every member of \(S-I\) belongs to \(S\); moreover \(0\notin S-I\), because \(I\ne S\). All \(t\ge2m\) belong to \(S-I\), as \(I\subseteq\mathbb N_0\). For \(t=m+i\in P\), addition to \(V\) cannot leave \(S\), while addition to \(U\) fails to remain in \(S\) exactly when \(t+x\in B\) for some \(x\in U\). Consequently, with
\[
Z=\bigcup_{x\in U}E_x,
\quad S-I=\{m+i:0\le i<L,\ i\notin Z\}\cup[2m,\infty).
\]
Every \(E_x\) is nonempty: for \(1\le x\le L+r-1=m-1\), its interval of possible indices intersects \([0,L-1]\).

**2. Compute the second quotient.** For every \(b\in B\), \(b+(S-I)\subseteq S\), since \(b+m\ge3m-r\ge2m+1\). For \(x\in[1,m-1]\), the only possible obstruction to \(x+(S-I)\subseteq S\) comes from \(m+i\in P\) with \(i\notin Z\), and is exactly the condition \(i\in E_x\). Thus \(x\in I^v\) if and only if \(E_x\subseteq Z\). Any negative integer \(y\) does not lie in \(I^v\): the member \(2m-1-y\ge2m\) of \(S-I\) produces the gap \(2m-1\) when added to \(y\). All of \(S\) belongs to \(I^v\). We conclude that
\[
I^v=S\cup B\cup\{x\in[1,m-1]:E_x\subseteq Z\}.
\]
When \(I=S\), instead \(S-I=S\) and \(I^v=S\), since \(0\in S\).

**3. Classify the fixed points.** Every nontrivial reflexive \(I\) must contain the full block \(B\). Writing \(Z=\bigcup_{x\in U}E_x\) as in step 1, the equality \(I=I^v\) holds exactly when \(U=\{x:E_x\subseteq Z\}\). The latter completion never changes \(Z\), because \(U\subseteq U_Z\) gives \(Z\subseteq\bigcup_{x\in U_Z}E_x\), while every \(E_x\) on the right is a subset of \(Z\). Conversely, for any union \(Z\) of windows, \(U_Z\) gives a normalized ideal \(I_Z\): its only potentially problematic sums \(x+(m+i)\in B\) are included, while sums with the full \(B\) or the conductor tail lie above the conductor. The quotient calculation gives \(I_Z^v=I_Z\). Every such \(Z\) is therefore realized; and different unions give different \(U_Z\), since \(Z=\bigcup_{x\in U_Z}E_x\). Moreover, \(Z\subseteq W\) implies \(U_Z\subseteq U_W\), and the converse follows by taking unions of the corresponding windows. Thus inclusion of ideals is inclusion of one-positions; union of two such supports is again a union of windows, proving the join statement.

**4. Translate window unions into binary words.** The windows \(E_x\) are all intersections of \([0,L-1]\) with translates of a length-\(r\) integer interval. A window strictly inside \([0,L-1]\) has exactly \(r\) points; a shorter window necessarily touches an endpoint. Every connected component of a union of windows that touches neither endpoint hence has at least \(r\) points. Conversely, a run touching an endpoint is covered by appropriately truncated sliding windows, and a run of length at least \(r\) strictly inside is covered by length-\(r\) windows. No windows spill outside the chosen runs. These statements remain valid for \(1\le L<r\), when all runs touch an endpoint. This proves the stated bijection with admissible words.

**5. Enumerate and determine growth.** The all-ones words contribute \(1/(1-z)\). Every other word has a unique initial run of ones, then a nonempty run of zeros, followed by zero or more repetitions of an interior run of at least \(r\) ones and a nonempty run of zeros, and finally an arbitrary terminal run of ones. The corresponding ordinary generating function is
\[
\frac1{(1-z)^2}\,\frac{z}{1-z}
\sum_{k\ge0}\left(\frac{z^{r+1}}{(1-z)^2}\right)^k
=\frac{z}{(1-z)((1-z)^2-z^{r+1})}.
\]
Putting \(D_r(z)=(1-z)^2-z^{r+1}\), the equation \(D_r(\rho_r)=0\) has a unique solution in \((0,1)\), by strict monotonicity of the two sides. There are no zeros of \(D_r\) in \(|z|<\rho_r\), since \(|1-z|\ge1-|z|\) and \((1-|z|)^2>|z|^{r+1}\). Equality on the circle \(|z|=\rho_r\) forces \(z=\rho_r\), so this is the unique dominant singularity. It is a simple pole because \(D_r'(\rho_r)=-2(1-\rho_r)-(r+1)\rho_r^r<0\). Its residue gives exactly the asymptotic coefficient stated in the finding. For increasing \(r\), the unique root \(\rho_r\) increases strictly, since \(\rho^{r+1}\) decreases strictly for fixed \(\rho\in(0,1)\), and \(\rho_r\to1\); thus the growth constants decrease to \(1\). For \(r=3\), \(D_3(z)=(1-z-z^2)(1-z+z^2)\), so \(\rho_3=(\sqrt5-1)/2\). This completes the proof.

## Verification
The accompanying standard-library script `verify.py` independently enumerates normalized relative ideals using direct addition closure, computes both ideal quotients from their definitions, and compares the complete resulting set of reflexive ideals (not merely counts) with the window-word construction. It also recomputes finite coefficients directly from words and independently by formal power-series inversion. Running `python verify.py` gives:

`VERIFY_OK cases=22 normalized_ideals=7985 direct_double_quotients=checked word_bijection=checked rational_series=checked`

The verified cases have \(3\le r\le6\) and positive \(L=m-r\) up to \(6\) for \(r=3,4,5\) and up to \(4\) for \(r=6\). For \(r=3\), the first nine \(a_3(L)\) values at \(L=1,\ldots,9\) are \(2,4,7,11,17,27,44,72,117\). Finite enumeration supplements, rather than substitutes for, the proof for all parameters.

## Relationship to prior work
Campochiaro, D’Anna and García-Sánchez define reflexive numerical-semigroup ideals through the double ideal quotient and develop general decomposition, Apéry-set and special-family criteria. Their 2026 manuscript supplies the motivating framework but does not state a terminal-gap, arbitrary-block-length binary-word classification or its rational counting series. An earlier result for the particular terminal-block length \(r=2\) gives a length-two forbidden-run classification; it is not claimed here. The present theorem instead handles every \(r\ge3\), including a common expression for all block lengths and their distinct growth rates. General enumerations of all semigroup ideals do not, by themselves, determine this divisorial subset.

## Limitations
The formula requires exactly one terminal interval of gaps immediately below twice the multiplicity and a positive initial interval of nongaps, with \(r\ge3\). It does not enumerate ideals of arbitrary numerical semigroups or ideals with multiple separated upper gap intervals, nor their full lattice operations. The coefficient asymptotic is for fixed \(r\) as \(m\to\infty\), not a uniform two-parameter asymptotic. No independent mathematical audit has been conducted.

## References
1. P. Campochiaro, M. D’Anna and P. A. García-Sánchez, *Reflexive ideals of a numerical semigroup*, arXiv:2610.06426v1, first publicly available October 5, 2026. https://arxiv.org/html/2610.06426v1
2. *Counting ideals in numerical semigroups*, arXiv:2304.13690, https://arxiv.org/abs/2304.13690. Background for counting ideals rather than for the specialized reflexive-window classification.
