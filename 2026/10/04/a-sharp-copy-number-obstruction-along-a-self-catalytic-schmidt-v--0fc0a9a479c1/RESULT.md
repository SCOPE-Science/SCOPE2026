# A sharp copy-number obstruction along a self-catalytic Schmidt-vector family

## Finding

Consider the one-parameter family of ordered Schmidt vectors
\[
\alpha(a)=
\left(
a,\,
\frac{247}{250}-a,\,
\frac{3}{500},\,
\frac{3}{500}
\right),
\qquad
\frac9{10}\le a<\frac{19}{20},
\]
and the target
\[
\beta=
\left(
\frac{19}{20},\,
\frac3{100},\,
\frac1{50},\,
0
\right).
\]

Suppose \(N\ge1\) copies of the source state itself are used as a catalyst. Deterministic LOCC conversion requires
\[
\alpha(a)^{\otimes(N+1)}
\prec
\beta\otimes\alpha(a)^{\otimes N}.
\]

A single majorization prefix forces the exact necessary condition
\[
\boxed{
N\ge
R(a):=
\frac{40a}
{(19-20a)(247-250a)}.
}
\]
Therefore any successful conversion needs at least
\[
\boxed{N\ge\lceil R(a)\rceil}
\]
catalyst copies.

This obstruction diverges at the upper endpoint:
\[
R(a)
=
\frac1{5(19/20-a)}
-\frac{104}{19}
+
O(19/20-a),
\qquad
a\uparrow\frac{19}{20}.
\]
Hence no fixed finite number of self-catalyst copies can work uniformly along this family.

The five multi-copy examples in Table I of Duarte, Drumond, and Terra Cunha lie exactly on this family. The obstruction gives
\[
\begin{array}{c|c|c}
a&R(a)&\lceil R(a)\rceil\\
\hline
0.900&18/11&2\\
0.908&227/105&3\\
0.918&459/140&4\\
0.925&296/63&5\\
0.928&928/165&6
\end{array}
\]
and the source independently records successful deterministic self-catalytic conversions using respectively
\[
2,3,4,5,6
\]
copies. Thus the same prefix inequality analytically certifies minimality of the copy count in every one of those five tabulated examples.

## Assumptions and scope

The vectors are Schmidt-coefficient probability vectors in decreasing order. A zero is appended to the three-component target so source and target products may be compared in a common dimension.

The integer \(N\) counts copies of \(\alpha(a)\) used as catalyst. Thus the complete source Schmidt vector is
\[
\alpha(a)^{\otimes(N+1)},
\]
while the complete target is
\[
\beta\otimes\alpha(a)^{\otimes N}.
\]

The theorem is a necessary copy-number obstruction on the entire continuous family. It does not assert that
\[
N=\lceil R(a)\rceil
\]
is sufficient at every value of \(a\). Sufficiency is used only for the five listed parameter values, where it is independently supplied by the source's successful conversion table and replayed by the packaged finite checker.

## Proof

Write
\[
b=\frac{247}{250}-a.
\]
On
\[
\frac9{10}\le a<\frac{19}{20},
\]
we have
\[
a>b>\frac3{500}>0.
\]

The largest entry of
\[
\alpha(a)^{\otimes(N+1)}
\]
is \(a^{N+1}\). The next \(N+1\) largest entries are precisely the products with one factor \(b\) and all other factors \(a\), each equal to
\[
a^N b.
\]
Therefore the sum of the largest \(N+2\) source entries is
\[
S_{N+2}
=
a^{N+1}+(N+1)a^N b
=
a^N\bigl[a+(N+1)b\bigr].
\]

For
\[
\beta\otimes\alpha(a)^{\otimes N},
\]
the largest entry is
\[
\frac{19}{20}a^N.
\]
The next \(N\) largest entries are
\[
\frac{19}{20}a^{N-1}b.
\]
After them comes
\[
\frac3{100}a^N.
\]
To justify this ordering, note that throughout the stated interval
\[
\frac{19}{20}\frac247/250 - aa>\frac3{100},
\]
while
\[
\frac3{100}
>
\frac{19}{20}\left(\frac ba\right)^2
\]
and
\[
\frac3{100}
>
\frac{19}{20}\frac{3/500}a.
\]
Thus the sum of the largest \(N+2\) target entries is
\[
T_{N+2}
=
\frac{19}{20}a^N
+
N\frac{19}{20}a^{N-1}b
+
\frac3{100}a^N
=
a^{N-1}
\left[
\frac{49}{50}a+\frac{19}{20}Nb
\right].
\]

Nielsen's deterministic pure-state LOCC criterion requires every ordered source prefix to be no larger than the corresponding target prefix. In particular,
\[
S_{N+2}\le T_{N+2}.
\]
After division by \(a^{N-1}>0\) and substitution of
\[
b=\frac{247}{250}-a,
\]
this becomes
\[
N(5000a^2-9690a+4693)\ge40a.
\]
The quadratic factorizes exactly:
\[
5000a^2-9690a+4693
=
(20a-19)(250a-247).
\]
For
\[
\frac9{10}\le a<\frac{19}{20},
\]
both factors on the right are negative, so their product is positive. Hence
\[
N\ge
\frac{40a}
{(19-20a)(247-250a)}.
\]

Finally, set
\[
\delta=\frac{19}{20}-a.
\]
Then
\[
19-20a=20\delta,
\qquad
247-250a=\frac{19}2+250\delta,
\]
and direct expansion gives
\[
R(a)
=
\frac1{5\delta}-\frac{104}{19}+O(\delta).
\]
This proves the divergence and therefore the absence of any uniform finite catalyst-copy budget on the family.

For the five source-table values, exact rational substitution gives the fractions displayed in the finding. Their ceilings match the source's recorded successful copy counts, so each recorded count is minimal.

## Verification

`verify_self_catalysis_bound.py` performs three independent checks.

First, it evaluates the closed-form obstruction using exact rational arithmetic at the five tabulated parameter values.

Second, it explicitly forms and sorts the full tensor-product Schmidt vectors for each of the five examples. It verifies that majorization succeeds at the source's stated copy count and fails for every smaller positive copy count.

Third, it checks that the failing prefix predicted by the proof has length \(N+2\) and that its exact difference has the claimed factorization.

These finite checks verify the table claims and the implementation. The continuous lower bound and its divergence are supplied by the analytic proof above.

## Relationship to prior work

Duarte, Drumond, and Terra Cunha introduced self-catalysis for bipartite pure-state conversion and asked whether multiple copies of the source itself can enable a conversion that fewer copies cannot. Their Table I gives five consecutive examples with target
\[
(0.950,0.030,0.020)
\]
and minimum catalyst-copy counts
\[
2,3,4,5,6.
\]
The source treats these as individual examples; it does not state the one-parameter family obstruction or the divergent closed-form lower bound above.

Earlier work by Duan, Feng, Li, and Ying established that arbitrarily many copies may be relevant in multiple-copy entanglement transformations. That is a broader existence statement for multiple-copy LOCC and catalysis. The present result is different: it gives an explicit quantitative lower bound for *self-catalysis* along the concrete family underlying the later paper's table and shows exactly why every one of its multi-copy rows needs the stated number of copies.

Targeted searches using the five Schmidt vectors, the common target, “self-catalysis,” “minimum copies,” “majorization,” and the exact affine family did not locate this prefix formula or its endpoint divergence.

## Limitations

The bound is necessary, not a global sufficient condition along the whole continuous family. It therefore does not classify every value of \(a\) by its exact minimum successful copy number.

The divergence result concerns this particular natural affine family extracted from the source's five multi-copy examples. It is not a universal lower bound for all self-catalytic state pairs.

The conclusion concerns deterministic LOCC between bipartite pure states. Stochastic conversion probabilities, mixed states, and multipartite transformations are outside the claim.

A residual literature risk remains because general majorization theory for multiple-copy transformations is extensive; an equivalent specialization may exist under different notation despite not appearing in the targeted searches.

## References

1. C. Duarte, R. C. Drumond, and M. Terra Cunha, “Self-catalytic conversion of pure quantum states,” arXiv:1504.06364, first submitted 23 April 2015; *Journal of Physics A: Mathematical and Theoretical* 49 (2016), 145303, DOI: 10.1088/1751-8113/49/14/145303.
2. R. Duan, Y. Feng, X. Li, and M. Ying, “Multiple-copy entanglement transformation and entanglement catalysis,” *Physical Review A* 71 (2005), 042319, arXiv:quant-ph/0404148, DOI: 10.1103/PhysRevA.71.042319.
3. M. A. Nielsen, “Conditions for a Class of Entanglement Transformations,” *Physical Review Letters* 83 (1999), 436–439, arXiv:quant-ph/9811053, DOI: 10.1103/PhysRevLett.83.436.
