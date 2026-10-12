# First generalized Frobenius number for triples of consecutive centered squares

## Finding

Define the centered-square numbers \(C_j=j^2+(j+1)^2=2j^2+2j+1\). For every integer \(n\ge3\), let \(g_1(n)\) be the greatest nonnegative integer possessing **at most one** triple \((x,y,z)\) of nonnegative integers with
\[
N=xC_n+yC_{n+1}+zC_{n+2}.
\]
Then the exact first generalized Frobenius number is
\[
\boxed{g_1(n)=\begin{cases}
506,&n=3,\\
6n^3+26n^2+43n+22,&n=4,5,\\
8n^3+20n^2+16n-2,&n\ge6.
\end{cases}}
\]

In fact, the theorem determines the complete second Apéry layer: the least integer in each residue class having **two distinct representations**. Put \(a=C_n\), \(b=C_{n+1}\), \(c=C_{n+2}\), and define the region
\[
L_n=\{(u,0):0\le u\le2n+2\}\cup
\{(u,v):0\le u\le2n-3,\ 1\le v\le n+1\}.
\]
Every residue \(r\pmod a\) has a unique pair \((u,v)\in L_n\) satisfying \(ub+vc\equiv r\pmod a\). Its first and second minimal nonnegative \(b,c\)-representatives are, respectively, \(ub+vc\) and \(ub+vc+\delta_n(u,v)a\), with
\[
\delta_n(u,v)=\begin{cases}
n+1,&u\ge5,\\
n+2,&u<5\text{ and }v=n+1,\\
2n+3,&\text{otherwise}.
\end{cases}
\]
Here distinct \(b,c\)-representatives mean distinct coefficient pairs, even if they yield equal integer weights. Their second minimum is well-defined. This explicit entire second layer implies the displayed piecewise maximum.

## Assumptions and scope

All parameters \(n\) are integers at least \(3\); \(x,y,z,u,v\) are nonnegative integers. Representations are counted by **distinct coefficient triples**, not by orderings of coins. The gcd of \(a\) and \(b\) is \(1\), hence every residue has representations and \(g_1(n)\) is finite. The ordinary Frobenius number \(g_0\), which excludes all representations, is different from the invariant \(g_1\) studied here.

A first or second representative in a residue is taken among all \(ub+vc\) with \(u,v\ge0\), including multiplicity if distinct pairs have equal weight. This convention matches the counting of triples at each integer \(N\): for every fixed pair \((u,v)\) in the same residue class, there is exactly one admissible value \(x=(N-ub-vc)/a\) once \(ub+vc\le N\).

## Proof

**1. Canonical representatives.** Write
\[
a=2n^2+2n+1,\quad b=2n^2+6n+5,\quad c=2n^2+10n+13.
\]
Because \(b-a=4(n+1)\), \(a\) is odd, and \(a\equiv1\pmod{n+1}\), we have \(\gcd(a,b)=1\). The following three identities hold identically:
\[
\begin{aligned}
(2n+3)b-(n+1)c&=(n+2)a,\\
(n+2)c-5b&=(n+1)a,\\
(2n-2)b+c&=(2n+3)a.
\end{aligned}
\]
For any coefficient pair \((u,v)\), each of the following reductions, when available, preserves its sum modulo \(a\) and strictly decreases it:
\[
\begin{array}{lll}
(u,v)\mapsto(u-(2n+3),v+(n+1)) &\text{if }u\ge2n+3,&\text{decrease }(n+2)a,\\
(u,v)\mapsto(u+5,v-(n+2)) &\text{if }v\ge n+2,&\text{decrease }(n+1)a,\\
(u,v)\mapsto(u-(2n-2),v-1)&\text{if }u\ge2n-2,\ v\ge1,&\text{decrease }(2n+3)a.
\end{array}
\]
Each resulting pair remains nonnegative. Termination follows from strict descent in the nonnegative weight \(ub+vc\). The terminal pairs are exactly those in \(L_n\). Since
\[
|L_n|=(2n+3)+(2n-2)(n+1)=a,
\]
and the residues of \(0,b,\ldots,(a-1)b\) cover all \(a\) residue classes, reduction makes the map \((u,v)\mapsto ub+vc\pmod a\) a bijection from \(L_n\) to all residues. Furthermore every pair reduces to its unique terminal pair while strictly decreasing weight, so \(ub+vc\) at the canonical pair is the **least** \(b,c\)-weight in its residue.

**2. Exact second representative by last-step reversal.** Fix \((u,v)\in L_n\) and write \(w=ub+vc\). Any different nonnegative pair giving the same residue lies outside \(L_n\), and any sequence of decreasing reductions ending at \((u,v)\) has a final reduction step. Reversing that final step from \((u,v)\) must be one of
\[
\begin{array}{lll}
(u,v)\mapsto(u+(2n+3),v-(n+1)),&v\ge n+1,&\text{increase }(n+2)a,\\
(u,v)\mapsto(u-5,v+(n+2)),&u\ge5,&\text{increase }(n+1)a,\\
(u,v)\mapsto(u+(2n-2),v+1),&\text{always},&\text{increase }(2n+3)a.
\end{array}
\]
Every applicable reverse move produces a different nonnegative coefficient pair with the same residue and exactly the shown increased weight. Conversely, any other pair must, on reduction to \((u,v)\), pass through a final step whose reversed increase is at least the least available increase, and earlier decreasing steps contribute additional positive weight differences. Therefore the least positive weight increase from \(w\) to a second pair is **exactly** the smallest available reverse-step cost. Since the only possible condition \(v\ge n+1\) inside \(L_n\) is \(v=n+1\), the minimum is precisely \(\delta_n(u,v)a\) with the three cases stated in the Finding.

At any integer \(N\equiv w\pmod a\), the number of distinct triples representing \(N\) equals the number of distinct \((u',v')\) of that residue with \(u'b+v'c\le N\), because the coefficient of \(a\) is then uniquely fixed. Thus the computed second \(b,c\)-weight is exactly the least integer of its residue having two representations. The largest integer with at most one representation is one less \(a\)-step than the maximum such threshold: \(g_1(n)=\max_{(u,v)\in L_n}\{ub+vc+\delta_n(u,v)a\}-a\).

**3. Maximize the three parts of the second layer.** For \(n\ge4\), the three cases of \(\delta_n\) have these respective maxima, using \(b,c>0\):
\[
\begin{aligned}
M_1&=(2n-3)b+(n+1)c+(n+1)a&&\text{(region }u\ge5),\\
M_2&=4b+(n+1)c+(n+2)a&&\text{(region }u<5,\ v=n+1),\\
M_3&=4b+nc+(2n+3)a&&\text{(region }u<5,\ v<n+1).
\end{aligned}
\]
All three corner pairs are admissible for \(n\ge4\). In the region \(u\ge5\), the maximum can lie on the \(v=0\) edge or on the \(v\ge1\) rectangle. The latter corner exceeds the former by \( (n+1)c-5b=2n^3+2n^2-7n-12>0\) for every \(n\ge3\): this polynomial equals \(39\) at \(n=3\) and has positive consecutive difference \(6n^2+10n-3\). Thus the stated \(M_1\) is indeed the largest in the whole \(u\ge5\) region. Expansion yields
\[
\begin{aligned}
M_1-a&=8n^3+20n^2+16n-2,\\
M_2-a&=4n^3+24n^2+50n+34,\\
M_3-a&=6n^3+26n^2+43n+22.
\end{aligned}
\]
Also \(M_2-M_3=-2n^3-2n^2+7n+12<0\) for every \(n\ge4\). To compare the other two, note
\[
M_1-M_3=2n^3-6n^2-27n-24.
\]
It is negative at \(n=4,5\) and positive at \(n=6\); its increment upon replacing \(n\) by \(n+1\) is \(6n^2-6n-31>0\) for every \(n\ge4\). Thus \(M_3\) wins exactly at \(n=4,5\), and \(M_1\) wins for all \(n\ge6\).

For \(n=3\), the special width \(2n-3=3\) means the region \(u<5\) has at most \(u=3\) when \(v>0\). Directly taking the largest corner in each of the three disjoint cases gives maximum second-representative candidates
\[
8b+4a=428,\qquad3b+4c+5a=492,\qquad3b+3c+9a=531,
\]
where \((a,b,c)=(25,41,61)\). The winning second representative is \(531\), giving \(g_1(3)=531-25=506\). This completes the proof for all \(n\ge3\).

## Verification

The standalone standard-library script `verify.py` enumerates nonnegative \((u,v)\)-pairs by their actual weights \(ub+vc\), retaining the first **two** weights for every residue modulo \(a\). This priority-queue method is distinct from the reduction argument in the proof. For every integer \(3\le n\le80\), it checks the entire proposed second Apéry layer, its residuewise formula, and the piecewise maximum. The saved output in `verification_output.txt` reports the exact count of checked residue values. Finite enumeration is not the proof of the unrestricted theorem.

## Relationship to prior work

Yin, Mu and Komatsu (2024) give explicit \(p\)-Frobenius formulas for consecutive generalized-star numbers \(qj(j-1)+1\), but their main results impose \(q\ge4\), or stronger restrictions at higher \(p\). Here the consecutive centered squares are the *excluded* case \(q=2\), at \(j=n+1\). Chatterjee and Narula's 2025 preprint on triples of centered triangular and centered square numbers reports ordinary Frobenius numbers and Sylvester numbers (the number of unrepresentable integers). Their publicly accessible abstract does **not** state a \(p=1\) formula, and the full text was not accessible for comparison; this remains a material bibliographic risk. The present result concerns the **second Apéry layer** and the exact transition from one to two representations, not the already treated ordinary Frobenius number. The classic treatment of consecutive ordinary squares or cubes concerns different generators; the OEIS centered-square Frobenius entry concerns only two generators. Generic parametric Frobenius eventual-quasi-polynomiality does not supply this explicit piecewise \(p=1\) result.

## Limitations

This theorem addresses the first generalized Frobenius number only, for three consecutive centered squares with \(n\ge3\). It does not provide higher representation thresholds or complete denumerants, and it does not assert novelty of the already studied ordinary Frobenius value. The full 2025 Chatterjee–Narula preprint, a directly relevant source on the same generators, was unavailable; although its abstract describes only ordinary Frobenius and Sylvester numbers, a hidden discussion of generalized thresholds cannot be ruled out. Also, unindexed literature may contain equivalent statements. No external or independent mathematical validation has been performed.

## References

1. R. Yin, J. Mu and T. Komatsu, *The p-Frobenius Number for the Triple of the Generalized Star Numbers*, preprint posted 29 July 2024, DOI 10.20944/preprints202407.2280.v1; *Symmetry* 16 (2024), 1090, DOI 10.3390/sym16081090.
2. T. Chatterjee and P. Narula, *Frobenius numbers for the triplets of the centered triangular numbers and centered square numbers*, preprint, May 2025, publicly indexed abstract at https://www.researchgate.net/publication/391463774_Frobenius_numbers_for_the_triplets_of_the_centered_triangular_numbers_and_centered_square_numbers (full text unavailable).
3. M. Lepilov, J. O'Rourke and I. Swanson, *Frobenius numbers of numerical semigroups generated by three consecutive squares or cubes*, *Semigroup Forum* 91 (2015), DOI 10.1007/s00233-014-9687-8.
4. OEIS A069760, *Frobenius number of the numerical semigroup generated by consecutive centered square numbers*, https://oeis.org/A069760 (two-generator problem).
5. B. H. Roune and K. Woods, *The Parametric Frobenius Problem*, arXiv:1502.06009 (2015), general eventual quasi-polynomial theorem.
