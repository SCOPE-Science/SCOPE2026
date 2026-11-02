# Sharp half-grid witnesses for rational non-expansive fuzzy propositional elimination

## Finding

**Half-grid elimination theorem.** Fix an integer \(d\geq1\), and write \(G_d=\{j/d:0\leq j\leq d\}\). For any term \(f\) in the non-expansive fuzzy **propositional** signature specified below, with disjoint finite sets of hidden variables \(H\) and retained variables \(Y\), every retained valuation \(v\in[0,1]^Y\) satisfies
\[
\sup_{u\in[0,1]^H}f(u,v)=\max_{u\in G_{2d}^{H}}f(u,v),\qquad
\inf_{u\in[0,1]^H}f(u,v)=\min_{u\in G_{2d}^{H}}f(u,v).
\]
Consequently the pointwise strongest upper interpolant and strongest lower interpolant obtained by forgetting \(H\) are expressible by finite propositional terms using no hidden variables and only the rational constants in \(G_{2d}\). The factor two is optimal **for every** \(d\): there is a one-variable term over \(G_d\) whose unique maximizing valuation and maximum truth value both have reduced denominator exactly \(2d\).

## Assumptions and scope

The underlying real truth domain is \([0,1]\). Terms are generated from variables, constants in \(G_d\), lattice conjunction \(a\wedge b=\min(a,b)\), disjunction \(a\vee b=\max(a,b)\), fuzzy negation \(\neg a=1-a\), and clipped constant shifts \(S_c(a)=[a+c]_0^1\), where \(c\in d^{-1}\mathbb Z\cap[-1,1]\) and \([t]_0^1=\min(1,\max(0,t))\). Negative shifts are truncated subtraction; positive shifts are truncated addition. Formulae are finite. The retained values are arbitrary real numbers, not restricted to a rational lattice. Empty hidden-variable sets are allowed, with the usual singleton-product convention.

For a term \(f\), define \((\exists H\,f)(v)=\sup_{u\in[0,1]^H}f(u,v)\) and \((\forall H\,f)(v)=\inf_{u\in[0,1]^H}f(u,v)\). These are pointwise uniform upper/lower propositional interpolants: the upper interpolant is the least function of retained variables dominating all hidden substitutions, and the lower interpolant the greatest function lying below all such substitutions. This finding does **not** address elimination inside modal operators, where hidden valuations at different worlds are coupled through accessibility.

## Proof

**Step 1: a restricted-literal max-min normal form.** Let \(\mathcal L_d\) be the family of constants in \(G_d\) and clipped unary functions \([x_i+a]_0^1\) and \([-x_i+b]_0^1\), where \(a,b\in d^{-1}\mathbb Z\); intercepts need not belong to \([0,1]\). Every term over the stated signature is a finite lattice expression in members of \(\mathcal L_d\), hence by distributivity a finite max of finite minima of these pieces. This follows inductively from the following identities, valid for all real \(t\) and \(-1\leq c\leq1\):
\[
1-[t]_0^1=[1-t]_0^1,
\]
\[
S_c([t]_0^1)=
\begin{cases}
\max\{c,[t+c]_0^1\},&0\leq c\leq1,\\
\min\{1+c,[t+c]_0^1\},&-1\leq c\leq0.
\end{cases}
\]
Negation swaps finite max and min, and a monotone shift distributes through both; every new constant remains in \(G_d\), and all new intercepts remain in \(d^{-1}\mathbb Z\). The empty max/min conventions give constants \(0,1\). The induction is purely propositional and uses no continuity approximation.

**Step 2: optimize a single conjunctive clause.** In a fixed minimum-clause, isolate all pieces involving a hidden variable \(x\). Write their positive slopes as \([x+a_j]_0^1\) and their negative slopes as \([-x+b_k]_0^1\). If only one sign occurs, the minimum of these pieces attains its maximum at \(x=1\) (only positive slopes) or \(x=0\) (only negative slopes); if none occurs, it is constant in \(x\). If both signs occur, put \(a=\min_j a_j\) and \(b=\min_k b_k\). The variable-dependent part is
\[
g(x)=\min\{[x+a]_0^1,[-x+b]_0^1\}.
\]
Since clipping is nondecreasing, \(g(x)=[\min(x+a,-x+b)]_0^1\). The unclipped minimum is an inverted-V function, increasing up to \(x=(b-a)/2\) and decreasing thereafter, so its clipped maximum occurs at \(x_*=[(b-a)/2]_0^1\); the endpoints are also legitimate candidates. All three points lie in \(G_{2d}\), because \(a,b\) lie in \(d^{-1}\mathbb Z\). Every other piece of the clause is independent of \(x\), so maximizing \(g(x)\) also maximizes the entire clause. Hidden variables are separable within this minimum-clause; choose a maximizing half-grid value independently for each hidden variable. Therefore every clause has a half-grid maximizing tuple for each fixed retained valuation \(v\).

**Step 3: recombine and construct the interpolants.** A finite max commutes with a finite supremum:
\[
\sup_u\max_{j} C_j(u,v)=\max_j\sup_u C_j(u,v).
\]
Select a maximizing half-grid tuple for a clause achieving the right-hand maximum. The resulting tuple also maximizes \(f\). Thus \(\exists H\,f\) equals the finite term
\[
\bigvee_{u\in G_{2d}^{H}}f(u,\cdot).
\]
Substitution introduces constants from \(G_{2d}\), and every shift can be represented using constants from \(G_{2d}\); in particular, the entire displayed term belongs to the same non-expansive propositional language over \(G_{2d}\). The infimum equality follows by applying the supremum theorem to \(\neg f\) and using \(\forall H\,f=\neg\exists H\,\neg f\). This proof holds for every finite \(H\), every term size, and all retained valuations simultaneously.

**Step 4: optimality for every denominator.** Let \(k=0\) if \(d=1\); \(k=1\) if \(d\geq2\) is even; \(k=2\) if \(d\geq3\) is odd. Consider
\[
f_d(x)=\min\{x,S_{k/d}(1-x)\}.
\]
Since \(0\leq k<d\), the increasing branch \(x\) and decreasing branch \(1-x+k/d\) meet uniquely at
\[
x_d=\frac{d+k}{2d}\in(0,1),\qquad \max_{x\in[0,1]}f_d(x)=x_d.
\]
The clipping in the second branch does not change the unique maximum. For \(d=1\), \(x_d=1/2\). For even \(d\), \(d+k=d+1\) is coprime to \(2d\); for odd \(d\geq3\), \(d+k=d+2\) is likewise coprime to \(2d\). Consequently the reduced denominator of \(x_d\) is exactly \(2d\). Any uniform witness grid \(G_s\) with \(s<2d\) misses the unique maximizing input. Moreover, evaluating a variable-free term with constants in \(G_d\) stays in \(G_d\), so its maximum value \(x_d\) cannot be represented without extending the rational constants. Both sharpness conclusions follow. \(\square\)

## Verification

The accompanying standalone `checker.py` uses exact rational arithmetic, independently evaluates the formula syntax and the restricted-literal normal form, and implements a clausewise quantifier elimination. It tested \(288\) pseudorandom expressions at denominators \(d=1,2,3,4\), including nested negations and clipped shifts; \(1152\) exact supremum/infimum comparisons of projected expressions against half-grid (and, for the supremum, finer-grid) evaluations; and the sharp-denominator family at every \(1\leq d\leq24\). Its final output is `ALL_CHECKS_OK; random_terms=288; sup_inf_comparisons=1152; sharp_denominators=24`. These finite tests corroborate the proof but are not presented as its replacement. Reproduce by running `python checker.py` with Python 3 standard library, from the extracted artifact directory.

## Relationship to prior work

Gebhart, Schröder, and Wild (2026) prove uniform interpolation for the **full** non-expansive fuzzy modal logic and explicitly describe a construction using sums, differences, clipping, and divisions by two; this establishes the background existence theorem, not a missing interpolation result. Their theorem is stronger with respect to the allowed language. Their Remark 20 gives a common-denominator accounting for **threshold-judgement interpolants**, whereas their subsequent pointwise formula construction explicitly uses division by two; the distinction is important because the present optimization theorem concerns pointwise formula elimination. This result is specifically quantitative and restricted to the propositional fragment: an exact fixed \(2d\)-grid for *all hidden variables and arbitrary depth*, and the matching sharpness obstruction for every \(d\). Their 2025 work introduced the propositional signature in fuzzy description logics. The elementary lattice-polynomial and minimax steps are acknowledged as the proof mechanism, rather than claimed as separate new discoveries. Searches did not establish a prior source explicitly proving this particular half-grid bound and the universal optimality family; earlier lattice-polynomial quantifier-elimination literature could conceivably imply it implicitly.

## Limitations

The theorem is about the rational-constant propositional sublanguage and real-valued semantics, not the full modal interpolation theorem. It does not cover arbitrary binary truncated addition, modal nesting, non-rational shifts, or infinite families of hidden variables. The constructive explicit interpolant can have size exponential in the number of hidden variables; this theorem claims a bound on *numerical precision*, not formula size. The originality comparison is limited by possible alternate formulations in historical lattice-polynomial and fuzzy logic literature. No independent scientific audit has been performed.

## References

1. S. Gebhart, L. Schröder, and P. Wild, *Non-Expansive Fuzzy Modal Logic Has Uniform Interpolation*, arXiv:2610.32335v1 (first posted 2026-10-23), especially Sections 2, 3, 6, 7, Remark 20, Theorems 21 and 23, and the relevant Appendix A interpolation proof. https://arxiv.org/html/2610.32335v1
2. S. Gebhart, L. Schröder, and P. Wild, *Non-expansive Fuzzy ALC*, arXiv:2505.09416 (first posted 2025-05-14). https://arxiv.org/abs/2505.09416
