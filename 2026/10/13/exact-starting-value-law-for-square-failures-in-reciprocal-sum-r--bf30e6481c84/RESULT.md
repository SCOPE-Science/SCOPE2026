# Exact starting-value law for square failures in reciprocal-sum recurrences

## Finding

Fix \(h\in\mathbb N\), set \(k=h^2\), and for a positive integer starting value \(x_0\) let
\[
x_{n+1}=\frac{h^2}{x_0+\cdots+x_n},
\]
with \(x_n=a_n/b_n\) in lowest terms. Let \(F_h(x_0)\) be the number of indices \(n\ge2\) for which \((2/h)a_n+b_n\) is not a perfect square.

Put
\[
P(h)=\{p\mid h:p=2\text{ or }p\equiv1\pmod4\},\qquad \alpha_p=v_p(h),
\]
and
\[
M_h=\prod_{p\in P(h)}p^{\alpha_p+1}.
\]
For \(p\in P(h)\), define \(T_p\) on \(\mathbb P^1(\mathbb F_p)\) by \(T_p(t)=t+t^{-1}\) for \(t\in\mathbb F_p^*\), with \(T_p(0)=T_p(\infty)=\infty\), and let
\[
B_{p,r}=\{t\in\mathbb F_p^*:T_p^r(t)=0\},\qquad c_{p,r}=|B_{p,r}|.
\]
Then the failed term indices are exactly
\[
\{r+1:\tau_p(x_0)=r<\infty\text{ for some }p\in P(h)\},
\]
where \(\tau_p(x_0)=r\) precisely when
\[
x_0\equiv p^{\alpha_p}\left(\frac{h}{p^{\alpha_p}}\right)t
 \pmod {p^{\alpha_p+1}}
\]
for some \(t\in B_{p,r}\). In particular, \(F_h(x_0)\) is exactly periodic modulo \(M_h\).

Set \(w_{p,r}=c_{p,r}\) and
\[
w_{p,\infty}=p^{\alpha_p+1}-\sum_r c_{p,r}.
\]
The natural density of positive integer starts with exactly \(j\) failed terms is
\[
\delta_j(h)=\frac1{M_h}
\sum_{\tau:\,|\{\tau_p<\infty\}|_{\mathrm{distinct}}=j}
\prod_{p\in P(h)}w_{p,\tau_p}.
\]
The cardinality here counts distinct finite hit times: two different primes hitting at the same time spoil the same term and therefore contribute only one failure.

For \(h=65\),
\[
B_{5,1}=\{2,3\},\quad B_{5,2}=\{1,4\},\quad B_{13,1}=\{5,8\},
\]
with all other first-hit sets empty. Hence \(M_{65}=4225\), and exactly \(3507\), \(714\), and \(4\) residue classes modulo \(4225\) have respectively \(0\), \(1\), and \(2\) failed terms.

## Assumptions and scope

The result concerns the square case \(k=h^2\) of the reciprocal-sum recurrence and positive integer starting values \(x_0\). It uses the notation \(x_n=a_n/b_n\) from the motivating paper. The density statement is for \(x_0\) ordered by ordinary size; exact periodicity implies the stated natural densities with an \(O(1)\) counting discrepancy on every initial interval.

No closed formula is asserted for the individual finite-field first-hit counts \(c_{p,r}\) as \(p\) varies. They are finite, exactly computable data for the map \(t\mapsto t+t^{-1}\) over \(\mathbb F_p\). The theorem converts those local data into the complete fixed-\(h\) distribution, including collisions where several primes spoil the same term.

## Proof

Write
\[
t_n=\frac{x_0+\cdots+x_n}{h}=\frac{u_n}{v_n}
\]
in lowest terms. The motivating paper proves
\[
u_{n+1}=u_n^2+v_n^2,\qquad v_{n+1}=u_nv_n,
\]
with no cancellation, and for \(n\ge1\),
\[
\frac2h a_{n+1}+b_{n+1}
 =\frac{(u_{n-1}+v_{n-1})^2}{\gcd(h,u_n)}.
\]
It further shows that the expression is a square exactly when \(\gcd(h,u_n)=1\), and that the \(u_n\) are pairwise coprime. Thus each prime divisor of \(h\) can spoil at most one term.

Fix a prime \(p\mid h\), write \(\alpha=v_p(h)\) and \(H=h/p^\alpha\), and put \(s=v_p(x_0)\). Initially
\[
u_0=\frac{x_0}{\gcd(x_0,h)},\qquad
v_0=\frac{h}{\gcd(x_0,h)}.
\]
If \(s<\alpha\), then modulo \(p\) one has \(u_0\ne0\) and \(v_0=0\). Hence \(v_1=0\), \(u_1=u_0^2\ne0\), and inductively \(p\nmid u_n\) for every \(n\ge1\). If \(s>\alpha\), then \(u_0=0\) and \(v_0\ne0\) modulo \(p\), so \(u_1=v_0^2\ne0\) and \(v_1=0\); again \(p\nmid u_n\) for every \(n\ge1\). Therefore a counted failure caused by \(p\) is possible only when \(s=\alpha\).

Assume now \(s=\alpha\). Cancellation of the common factor in \(u_0/v_0\) gives
\[
\frac{u_0}{v_0}\equiv
\left(\frac{x_0}{p^\alpha}\right)H^{-1}\pmod p.
\]
As long as the affine ratio is defined and nonzero, the recurrence reduces to
\[
\frac{u_{n+1}}{v_{n+1}}
 =\frac{u_n^2+v_n^2}{u_nv_n}
 =\frac{u_n}{v_n}+\frac{v_n}{u_n},
\]
so modulo \(p\) the ratio follows \(T_p(t)=t+t^{-1}\). If the ratio reaches \(0\) at time \(r\), then \(p\mid u_r\) and \(p\nmid v_r\); at the next step the projective ratio is \(\infty\) and remains there. Hence first-hit times are disjoint and \(p\mid u_r\) exactly when the starting residue belongs to \(B_{p,r}\).

The congruence for the starting ratio is equivalent to
\[
x_0\equiv p^\alpha Ht\pmod{p^{\alpha+1}},
\]
so each \(t\in B_{p,r}\) gives exactly one residue class modulo \(p^{\alpha+1}\). If \(p\equiv3\pmod4\), a first hit cannot occur because a predecessor of \(0\) would satisfy \(t^2=-1\) in \(\mathbb F_p\); this is why only \(P(h)\) appears.

For distinct primes the local congruence moduli \(p^{\alpha_p+1}\) are pairwise coprime. The Chinese remainder theorem therefore makes the local states independent over one period \(M_h\). A state \(r\) for prime \(p\) has exactly \(c_{p,r}\) local residue classes, while the no-hit state has \(p^{\alpha_p+1}-\sum_r c_{p,r}\). Multiplying these local counts and grouping state tuples by the number of distinct finite hit times gives the formula for \(\delta_j(h)\). This also proves exact periodicity.

## Verification

The accompanying script implements the projective map, local congruence criterion, and the original integer recurrence independently. It exhaustively compares the predicted and directly observed failed-term sets for every \(1\le h\le60\) over one complete predicted period, totaling \(16182\) starting residues. It then exhausts all \(4225\) residues for \(h=65\).

The replay output is:

`VERIFY_OK exhaustive_h_le_60_states=16182 h65_counts=3507,714,4 modulus=4225 B5={2: [1, 4], 1: [2, 3]} B13={1: [5, 8]}`

These finite computations corroborate the theorem and the numerical example; the universal statement is proved by the valuation, finite-field dynamics, and Chinese-remainder argument above rather than by enumeration.

## Relationship to prior work

Matijasevick, Rodríguez, and Salazar prove the no-cancellation recurrence for \((u_n,v_n)\), the exact square criterion through \(\gcd(h,u_n)\), and the fact that each prime divisor of \(h\) can spoil at most one term. Their discussion identifies the finite-field dynamics of \(t\mapsto t+t^{-1}\) and asks for the proportion of starting values producing exactly a prescribed number of failures. The present result answers that fixed-\(h\) distribution question by identifying the precise prime-power congruence classes for each first-hit time and combining them by the Chinese remainder theorem.

Jones and Manes study Galois actions on infinite preimage trees of quadratic rational maps, including the family containing scalar multiples of \(t+t^{-1}\). That global arboreal framework does not provide the integer-start periodic law, prime-power congruence classification, or the collision-aware fixed-\(h\) density formula proved here.

Searches for aliases involving reciprocal-sum square failures, finite-field preimages of zero for \(t+t^{-1}\), first-hit distributions, and Chinese-remainder densities did not reveal a result implying the theorem. This is evidence from the inspected literature and search index, not a claim of exhaustive bibliographic uniqueness.

## Limitations

The theorem determines the complete distribution for every fixed \(h\) once the finite sets \(B_{p,r}\) are known, but it does not give a uniform closed form for \(c_{p,r}\) as \(p\) varies, nor asymptotics in a regime where \(h\) itself grows. It also does not address the perturbed recurrences associated with other quadratic fields in the motivating paper.

The computational replay checks many finite cases but is not used as an infinite proof. Bibliographic searches can miss differently phrased or inaccessible work; the principal residual originality risk is prior finite-field dynamical literature that may encode equivalent first-hit counts in another language.

## References

1. Mateo Matijasevick, Santiago Rodríguez, Gregorio Salazar, *Perfect squares in reciprocal-sum sequences and primes that are inert in quadratic fields*, arXiv:2610.00765v1, 2026.
2. Rafe Jones, Michelle Manes, *Galois theory of quadratic rational functions*, Commentarii Mathematici Helvetici 89 (2014), 173–213, DOI 10.4171/CMH/316; arXiv:1101.4339.
