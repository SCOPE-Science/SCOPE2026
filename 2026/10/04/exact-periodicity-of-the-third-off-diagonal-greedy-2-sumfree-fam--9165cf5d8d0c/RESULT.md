# Exact periodicity of the third off-diagonal greedy 2-sumfree family

## Finding
For integers \(f<g\), let \(S_{f,g}\) be the increasing strict greedy 2-sumfree sequence beginning with \(f,g\): after the prescribed first two terms, the next term is the least larger positive integer that is not a sum of two distinct earlier terms.

For every integer \(f\ge 6\), put
\[
M=5f+5,
\qquad
E=\{f\}\cup[2f+3,3f+2],
\]
and define the residue set modulo \(M\)
\[
R=[f-2,f]\cup[2f+4,3f]\cup[4f+3,4f+6].
\]
Then
\[
S_{f,2f+3}
=E\cup\Bigl(\{n\ge4f+3:n\bmod M\in R\}\setminus\{6f+3,11f+8\}\Bigr)\cup\{8f+6\}.
\]
Thus the third off-diagonal family has a periodic tail with modulus \(5f+5\), but unlike the first two off-diagonal families it has three transient corrections: the periodic prediction contains \(6f+3\) and \(11f+8\), which are excluded, while \(8f+6\) is inserted.

The eventual cyclic first-difference word, starting at residue \(f-2\), is
\[
(1,1,f+4,1^{f-4},f+3,1,1,1,2f-3).
\]
It has \(f+4\) entries and total sum \(M\). Its minimal period length is \(f+4\), and the natural density is
\[
\frac{f+4}{5f+5}.
\]

## Assumptions and scope
All intervals are integer intervals and are inclusive. The operation defining the sequence forbids only sums of two distinct earlier sequence elements. The theorem is uniform for \(f\ge6\); the small case \(f=5\) follows a different transient pattern and is not included.

The proof is entirely elementary. Computation is used only as a corroborative check of the closed form, not to infer the infinite theorem.

## Proof
Let
\[
I=[2f+3,3f+2],\qquad
A=[f-2,f],\qquad
B=[2f+4,3f],\qquad
C=[4f+3,4f+6],
\]
so that \(E=\{f\}\cup I\) and \(R=A\cup B\cup C\). Let \(P\) be the set of integers \(n\ge4f+3\) whose residue modulo \(M\) lies in \(R\). Set
\[
a=6f+3,\qquad x=8f+6,\qquad c=11f+8,
\]
and define
\[
T=E\cup(P\setminus\{a,c\})\cup\{x\}.
\]
We prove that \(T\) is exactly the greedy sequence.

First, the initial greedy segment is \(E\). Indeed, before \(f+(2f+3)=3f+3\) there is no sum of two distinct selected terms, so all of \([2f+3,3f+2]\) are selected. The next gap is
\[
[3f+3,4f+2]=f+I,
\]
so \(4f+3\) is the first possible subsequent term.

The key modular identity is
\[
(E+R)\bmod M=\{0,1,\ldots,M-1\}\setminus R.
\]
To verify it, the six elementary sums are
\[
\begin{aligned}
f+A&=[2f-2,2f],\\
f+B&=[3f+4,4f],\\
f+C&=[5f+3,5f+6],\\
I+A&=[3f+1,4f+2],\\
I+B&=[4f+7,6f+2],\\
I+C&=[6f+6,7f+8].
\end{aligned}
\]
Reducing modulo \(M=5f+5\), their union is exactly
\[
[0,f-3]\cup[f+1,2f+3]\cup[3f+1,4f+2]\cup[4f+7,5f+4],
\]
which is the complement of \(R\).

Also \((R+R)\bmod M\) is disjoint from \(R\). This follows from
\[
\begin{aligned}
A+A&=[2f-4,2f],\\
A+B&=[3f+2,4f],\\
A+C&=[5f+1,5f+6],\\
B+B&=[4f+8,6f],\\
B+C&=[6f+7,7f+6],\\
C+C&=[8f+6,8f+12],
\end{aligned}
\]
after reduction modulo \(M\). For \(f\ge6\), every resulting interval lies in one of the four complementary intervals displayed above or in a subinterval disjoint from \(R\).

These two modular facts show that no member of \(P\) can be a sum of a member of \(E\) and a member of \(P\), or of two members of \(P\). The only conflict coming from two finite initial terms is
\[
I\mathbin{\widehat{+}}I=[4f+7,6f+3],
\]
where the hat denotes sums of distinct elements. This meets \(P\) only at its endpoint \(a=6f+3\), explaining the first deletion.

The exceptional insertion \(x=8f+6\) is eligible. Before \(x\), the selected blocks outside \(E\) are
\[
[4f+3,4f+6],\qquad [6f+4,6f+5],\qquad [7f+9,8f+5].
\]
No pair from these blocks and \(E\) sums to \(x\): two elements of \(E\) sum to at most \(6f+4\); subtracting an element of \([4f+3,4f+6]\) from \(x\) gives \([4f,4f+3]\), outside \(E\); subtracting an element of \([6f+4,6f+5]\) gives \(\{2f+1,2f+2\}\), also outside \(E\); and the smallest sum of two distinct elements of \([4f+3,4f+6]\) is \(8f+7\). Any pair involving \([7f+9,8f+5]\) and another positive selected term is larger than \(x\).

Modulo \(M\), the exceptional residue is
\[
x\equiv3f+1\pmod M.
\]
Its sums with \(R\) reduce to
\[
[4f-1,4f+1]\cup[0,f-4]\cup[2f-1,2f+2],
\]
which is disjoint from \(R\). Hence \(x\) creates no conflict with the periodic tail. On the other hand,
\[
x+E=\{9f+6\}\cup[10f+9,11f+8]
\]
meets \(P\) exactly at \(c=11f+8\). This explains the second deletion. Therefore every element of \(T\) is eligible when it is reached.

It remains to show that every integer omitted from \(T\) is forbidden. Up through the second complete periodic block, the gaps are covered by explicit earlier sums:
\[
\begin{aligned}
[3f+3,4f+2]&=f+I,\\
[4f+7,6f+3]&=I\mathbin{\widehat{+}}I,\\
[6f+6,7f+8]&=I+[4f+3,4f+6],\\
[8f+7,9f+7]&=I+[6f+4,6f+5],\\
[9f+12,11f+8]&=I+[7f+9,8f+6],\\
[11f+11,12f+13]&=I+[9f+8,9f+11].
\end{aligned}
\]
The next gap is
\[
[13f+11,14f+12],
\]
and it is covered by the union of
\[
[4f+3,4f+6]+[9f+8,9f+11]
\]
and
\[
I+[11f+9,11f+10].
\]
All displayed representations use distinct earlier selected terms.

Now let \(n\ge14f+17\) be an integer whose residue is outside \(R\). By the identity \((E+R)\bmod M=R^{\mathrm c}\), choose \(e\in E\) so that \(n-e\) has residue in \(R\). Since \(e\le3f+2\),
\[
n-e\ge11f+15>11f+8=c.
\]
Thus \(n-e\) lies in the uncorrected periodic tail \(P\setminus\{a,c\}\), and it is smaller than \(n\). Hence \(n=e+(n-e)\) is forbidden. This proves by induction that the greedy construction selects exactly \(T\).

Finally, after the last transient deletion, the selected residues in one modulus are \(A,B,C\), whose cyclic first differences are
\[
(1,1,f+4,1^{f-4},f+3,1,1,1,2f-3).
\]
For \(f=6\), the gap \(f+4\) occurs uniquely; for \(f=7\), the gap \(f+3\) occurs uniquely; and for \(f\ge8\), the gap \(2f-3\) is uniquely largest. Hence the cyclic word is primitive, so the minimal eventual first-difference period has length \(f+4\). Since \(|R|=f+4\), the density is \((f+4)/(5f+5)\).

## Verification
The accompanying `verify.py` independently constructs the greedy sequence using exact integer arithmetic and compares it with the theorem for every \(6\le f\le200\) through twenty modulus lengths. It also checks, for each tested \(f\), the exact modular complement identity \((E+R)\bmod M=R^{\mathrm c}\), the disjointness \((R+R)\cap R=\varnothing\), the exceptional-residue disjointness, and \(|R|=f+4\). Its deterministic output is

`VERIFY_OK f_cases=195 range=6..200 periods=20`

These computations are finite corroboration. The infinite statement follows from the interval and modular proof above.

## Relationship to prior work
Van Berkel and Bosma introduced the current systematic study of greedy strict \(2\)-sumfree sequences and proved ultimate periodicity in a substantial parameter region. Their companion paper formulates precise periodicity conjectures for all pairs \((f,g)\) and supplies extensive finite computational evidence. The publicly available record for that paper states that the earlier theorem covers \(f+1\le g<2f\); subsequent work covers the diagonal \(g=2f\).

The closest published extensions found in the literature and published-finding corpus are the first two off-diagonal families \(S_{f,2f+1}\) and \(S_{f,2f+2}\), with moduli \(5f+1\) and \(5f+3\), and the separate second-diagonal family \(S_{f,3f}\). None implies the present family: the parameter line \(g=2f+3\) is disjoint from the first two off-diagonal lines, and \(g=3f\) coincides with it only at \(f=3\), outside the theorem's range. Targeted searches for \(S_{f,2f+3}\), the modulus \(5f+5\), the period length \(f+4\), and the transient triple \(6f+3,8f+6,11f+8\) found no prior infinite proof.

The transient correction is mathematically substantive: simply extrapolating the residue formula from the first two off-diagonal families predicts the wrong early behavior. The new residue set gains a third low residue, and two periodic candidates must be deleted while one nonperiodic value must be inserted before the stable tail begins.

## Limitations
The theorem treats only the line \(g=2f+3\) for \(f\ge6\). It does not settle the general ultimate-periodicity conjecture or classify later off-diagonal lines. The case \(f=5\) has a different transient pattern and is intentionally excluded.

The main residual originality risk is historical or very recent work not indexed under modern strict-2-sumfree terminology. In particular, the full 1972 paper of Queneau was not materially inspected here. The recent literature's historical discussion and the targeted searches above did not reveal an infinite theorem equivalent to the present line, but that bibliographic risk remains.

## References
1. D. van Berkel and W. Bosma, *On t-sumfree sequences*, arXiv:2609.16843 (2026), first submitted 15 September 2026.
2. D. van Berkel and W. Bosma, *Periodicity conjectures for all 2-sumfree sequences*, arXiv:2609.18522 (2026), first submitted 16 September 2026.
3. *Exact periodicity of the first two off-diagonal greedy 2-sumfree families*, published-finding corpus record `2026/9/20/SCOPE-first-two-off-diagonal-2-sumfree-families--dc29809f76be`.
4. *Exact periodicity of the strict greedy 2-sumfree family \(S_{f,2f+1}\)*, published-finding corpus record `2026/9/17/SCOPE-periodicity-of-greedy-2-sumfree-s-f-2f-plus-1--211ee0999b72`.
5. R. Queneau, *Sur les suites s-additives*, J. Combin. Theory Ser. A 12 (1972), 31–71.
