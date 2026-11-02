# Exact density and critical carry threshold for single-colour g-adic sumsets

## Finding

Let \(g\ge2\) be an integer, let \(W\subseteq\mathbb N_0\) be infinite with infinite complement, and define the positive integer set
\[
A_g(W)=\left\{\sum_{i\in F} d_i g^i:\ \varnothing\ne F\subseteq W\text{ finite},\quad 1\le d_i\le g-1\right\}.
\]
For a positive integer \(h\), \(hA_g(W)\) means the sumset of exactly \(h\) members of \(A_g(W)\), with repetitions permitted. The natural density of \(S\subseteq\mathbb N_0\) is \(d(S)=\lim_{x\to\infty}|S\cap[0,x)|/x\), when the limit exists.

Write the unique decomposition of \(W\) into maximal consecutive runs as
\[
W=\bigsqcup_{j\ge1}[a_j,b_j]\cap\mathbb N_0,\qquad
L_j=b_j-a_j+1,\qquad t_j=a_{j+1}-b_j-1\ge1.
\]
(The runs are finite because the complement of \(W\) is infinite.) Then every sumset \(hA_g(W)\) with \(1\le h<g\) has natural density zero. At the first remaining summand count, the natural density **always exists**, and is exactly
\[
\boxed{\ d\bigl(gA_g(W)\bigr)=
 g^{-a_1}\,g^{-\sum_{j\ge1}(t_j-1)}
 \prod_{j\ge1}\left(1-\frac{g-1}{g^{L_j+1}}\right).\ }
\]
Here \(g^{-\infty}=0\), and all infinite products mean limits of finite prefix products. In particular,
\[
\boxed{\ d\bigl(gA_g(W)\bigr)>0\quad\Longleftrightarrow\quad
 \sum_{j\ge1}(t_j-1)<\infty\quad\text{and}\quad
 \sum_{j\ge1}g^{-L_j}<\infty.\ }
\]
Since the first sum consists of nonnegative integers, its finiteness means that all but finitely many gaps have length exactly one. These criteria are exact for arbitrary infinite coinfinite \(W\), without periodicity assumptions. They mark a strict transition: every smaller sum count has density zero, but some critical sumsets have density arbitrarily close to one.

More precisely, for any \(\varepsilon>0\) and fixed \(g\ge2\), choose one missing digit position between successive runs and run lengths \(L_j=N+j^2\) (\(j\ge1\)), starting at \(a_1=0\). Then \(W\) is infinite and coinfinite, and for sufficiently large \(N\),
\[
1-\varepsilon<d\bigl(gA_g(W)\bigr)<1.
\]

## Assumptions and scope

All integers are nonnegative unless explicitly described as positive. The set \(W\) is fixed, infinite, and has infinitely many excluded digit positions. The base \(g\) is an arbitrary fixed integer at least two, not necessarily prime. The index \(j\) runs over the maximal finite consecutive blocks of allowed exponents, ordered increasingly. The theorem concerns a single restricted-digit colour \(A_g(W)\), not the union across different partition classes, and it makes no statement about minimality of an additive basis.

## Proof

**1. Exact carry-block decomposition.** Put \(A_g^0(W)=A_g(W)\cup\{0\}\) and \(B_g(W)=gA_g^0(W)\). On the allowed run \([a_j,b_j]\), the \(g\)-adic digits of a single summand form an arbitrary integer \(X_j\) between zero and \(g^{L_j}-1\), multiplied by \(g^{a_j}\). The sum of \(g\) such interval-valued contributions fills the whole interval from zero to \(g(g^{L_j}-1)\). Consequently,
\[
B_g(W)=\left\{\sum_{j\ge1} g^{a_j}T_j:\
0\le T_j\le g(g^{L_j}-1),\ T_j\in\mathbb Z,\ T_j=0\text{ eventually}\right\}.
\]
This is an exact equivalence: choosing a permitted \(T_j\) can be achieved by distributing it among \(g\) integers in \([0,g^{L_j}-1]\), independently for each run, and then reading each row as one member of \(A_g^0(W)\). Conversely every such sum yields these \(T_j\).

Since \(g(g^{L_j}-1)=g^{L_j+1}-g<g^{L_j+1}\), the base-\(g\) digits of the contribution from run \(j\) occupy only positions \([a_j,b_j+1]\). The next run starts at \(a_{j+1}\ge b_j+2\), so distinct run contributions have disjoint digit supports and the above expression is unique. Between these enlarged blocks there are exactly \(t_j-1\) positions that must be zero.

**2. Finite-prefix densities.** For \(J\ge1\), let \(C_J\) consist of all nonnegative integers obeying the conditions from the first \(J\) enlarged blocks, with no restrictions at higher positions: all digits below \(a_1\) are zero; each block number \(T_j\), for \(1\le j\le J\), belongs to \([0,g^{L_j+1}-g]\); and all \(t_j-1\) intermediate digits between enlarged blocks are zero for \(j<J\). Then \(C_J\) is periodic modulo \(g^{b_J+2}\), contains \(B_g(W)\), and has exact natural density
\[
D_J=g^{-a_1-\sum_{j<J}(t_j-1)}
\prod_{j=1}^{J}\left(1-\frac{g-1}{g^{L_j+1}}\right).
\]
Indeed the enlarged block of length \(L_j+1\) admits exactly \(g^{L_j+1}-g+1\) out of its \(g^{L_j+1}\) digit words. The sequence \((D_J)\) decreases to the product \(D\) in the finding. If \(D=0\), then \(0\le\limsup_{x\to\infty}|B_g(W)\cap[0,x)|/x\le D_J\) for each \(J\), hence \(d(B_g(W))=0\).

**3. Positive-product case and genuine natural density.** Suppose \(D>0\). Then only finitely many \(t_j\) exceed one, and \(\sum_j\delta_j<\infty\), where
\[
\delta_j=\frac{g-1}{g^{L_j+1}}.
\]
Choose \(J\) beyond the last gap of length greater than one. After enlarged block \(J\), every later digit position belongs to one of the enlarged blocks, so any member of \(C_J\setminus B_g(W)\) must fail the upper bound for some later block. Let \(E_j\) be the set of nonnegative integers whose length-\(L_j+1\) block at positions \([a_j,b_j+1]\) represents one of the forbidden last \(g-1\) integers in \([0,g^{L_j+1}-1]\). Set \(q_j=g^{a_j+L_j+1}\). The set \(E_j\) is periodic modulo \(q_j\) and has exactly \((g-1)g^{a_j}\) forbidden residues in each period, so its periodic density is \(\delta_j\). Its least member is \((g^{L_j+1}-g+1)g^{a_j}>q_j/2\). For \(x>0\), no element of \(E_j\) occurs below \(x\) when \(q_j>2x\); if \(q_j\le2x\), the elementary period count yields
\[
|E_j\cap[0,x)|\le\left(\frac{x}{q_j}+1\right)(g-1)g^{a_j}\le3x\delta_j.
\]
Since \(C_J\setminus B_g(W)\subseteq\bigcup_{j>J}E_j\), the union bound gives
\[
0\le |(C_J\setminus B_g(W))\cap[0,x)|\le3x\sum_{j>J}\delta_j.
\]
Taking upper and lower limiting densities, and then \(J\to\infty\), proves \(d(B_g(W))=\lim_JD_J=D\). This proves ordinary natural density, not merely density along powers of \(g\) or logarithmic density.

**4. Removing zero summands.** In the unique block expression for \(n\in B_g(W)\), define \(s(n)=\sum_jT_j\). An expression as a sum of \(g\) nonzero members of \(A_g(W)\) is possible exactly when \(s(n)\ge g\). Necessity is clear because each nonzero row contributes at least one to the total of all block coordinates. For sufficiency, start with any distribution of the \(T_j\) among \(g\) rows with each coordinate between zero and \(g^{L_j}-1\). If one row is zero and \(s(n)\ge g\), at least one nonzero row has coordinate sum at least two. Transfer one coordinate unit from that donor row to the zero row in a block where the donor coordinate is positive; the donor stays nonzero and the recipient becomes nonzero. Repeat to obtain \(g\) nonzero rows without changing any \(T_j\). Therefore
\[
B_g(W)\setminus gA_g(W)=\{n\in B_g(W):s(n)<g\}.
\]
If \(n<x\), only runs with \(a_j<\log_g x\) can contribute, so the exceptional set with total block-coordinate sum at most \(g-1\) has \(O_g((1+\log x)^{g-1})\) elements below \(x\). This is density zero, and hence \(d(gA_g(W))=D\).

**5. Positive criterion and smaller sums.** The factors \(1-\delta_j\) are uniformly positive, with \(0<\delta_j\le (g-1)/g^2<1\). Their infinite product is positive if and only if \(\sum_j\delta_j<\infty\), equivalently \(\sum_jg^{-L_j}<\infty\). The other factor is positive if and only if \(\sum_j(t_j-1)<\infty\).

Finally fix \(1\le h<g\). When adding \(h\) base-\(g\) integers, the carry into any digit position is at most \(h-1\), by induction on the digit position. At each index outside \(W\), the corresponding input digits of all summands vanish. Thus the output digit there belongs to \(\{0,\ldots,h-1\}\), and can never be any of the \(g-h\) larger digits. Imposing this restriction at the first \(m\) excluded indices gives a periodic superset of \(hA_g(W)\) of density exactly \((h/g)^m\). Since the complement of \(W\) is infinite, \(m\) is arbitrary, proving \(d(hA_g(W))=0\).

**6. Densities approaching one.** Take \(a_1=0\), all \(t_j=1\), and \(L_j=N+j^2\). The formula becomes \(\prod_{j\ge1}(1-(g-1)g^{-N-j^2-1})\). It is positive, smaller than one, and tends to one as \(N\to\infty\), because the sum of factor defects tends to zero. This completes the proof.

## Verification

The accompanying `artifacts/verify.py` checks the finite-run block representation in three independent ways: direct enumeration of the restricted-digit set followed by repeated sumsets; complete enumeration of the permitted independent block coordinates; and the exact multiplicative block count. It checks seven concrete digit patterns for bases two, three, and four and directly tests the prohibited-digit carry restriction at every smaller summand count. Its expected final line is `VERIFY_OK finite_cases=7 independent_forms=3 exact_integer_arithmetic=yes`. These finite tests do not establish the infinite product or the existence of the natural density; those follow from the preceding proof.

## Relationship to prior work

Tang's 2026 paper establishes minimality of **unions over disjoint digit-position classes** when the base exceeds the number of summands and records a boundary obstruction at equality. Its carry lemma bounds carries in arbitrary sums. The present result instead asks for the density of a **single-class self-sumset** precisely at the critical count equal to the base, and supplies an exact arbitrary-run infinite product and necessary-and-sufficient positive-density criterion. The bounded-carry argument below the threshold is elementary and consistent with Tang's lemma; no originality is claimed for the carry bound alone.

Ling and Tang (2015), Sun and Tao (2019), and subsequent work study minimal asymptotic bases constructed from multiple classes, not the exact general single-class density formula established here. The Sun–Tao source was accessible only through its abstract and opening preview, so it cannot be excluded as implicit prior coverage on the strength of those excerpts alone. Glasscock, Moreira, and Richter (2024) analyze dimensions and sumsets of multiplicatively invariant integer sets; their same-base iterated-sumset dimension statements do not determine the present exact density for arbitrary nonperiodic position masks. Priority is not independently certified.

## Limitations

The theorem assumes \(W\) and its complement are both infinite, and treats integer bases \(g\ge2\). It does not describe densities for more than \(g\) summands, mixed-colour sumsets, minimality of unions, or representation-count distributions. The exact formula itself is proved for arbitrary runs, but historical originality is provisional pending specialist comparison, especially with the full Sun–Tao (2019) article and potentially unindexed work. The finite verifier supplies reproducible consistency checks, not a substitute for the infinite proof. No independent mathematical audit has been performed.

## References

1. M. Tang, *Minimal asymptotic g-adic bases from arbitrary partitions*, arXiv:2610.23152v1, first publicly submitted 16 October 2026, https://arxiv.org/abs/2610.23152 .
2. D. Ling and M. Tang, *On minimal asymptotic g-adic bases*, Bull. Aust. Math. Soc. 92 (2015), 374–379, doi:10.1017/S0004972715000805 .
3. C.-F. Sun and T.-T. Tao, *On g-adic minimal asymptotic bases of order h*, Int. J. Number Theory 15 (2019), 389–406, doi:10.1142/S1793042119500209 .
4. D. Glasscock, J. Moreira, and F. K. Richter, *Additive and geometric transversality of fractal sets in the integers*, J. Lond. Math. Soc. 109 (2024), e12902, doi:10.1112/jlms.12902 .
