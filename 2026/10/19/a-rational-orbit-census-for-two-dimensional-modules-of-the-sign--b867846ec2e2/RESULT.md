# A rational orbit census for two-dimensional modules of the sign quantum plane

## Finding

Let \(k=\mathbb F_q\), where \(q\) is an **odd prime power**, and let \(A=k\langle u,v\rangle/(uv+vu)\). The number of isomorphism classes of two-dimensional unital left \(A\)-modules over \(k\) is exactly
\[
\boxed{4q^2+q-2}.
\]
Equivalently, exactly this many simultaneous \(\mathrm{GL}_2(k)\)-conjugacy orbits occur among ordered pairs \((X,Y)\in M_2(k)^2\) satisfying \(XY+YX=0\). This is an **unweighted orbit count**, not the already known number of labeled anticommuting pairs.

More precisely, normalizing the first matrix \(X\) to rational canonical form yields the following disjoint, exhaustive classification. In the third column, an orbit means an orbit of the centralizer of the fixed \(X\) acting on the permissible \(Y\)'s.

| Similarity type of \(X\) | Number of \(X\)-classes | Number of compatible \(Y\)-orbits per class |
| --- | ---: | ---: |
| \(X=0\) | \(1\) | \(q^2+q\) |
| Nonzero scalar | \(q-1\) | \(1\) |
| Nonzero nilpotent Jordan block | \(1\) | \(2q-1\) |
| Trace-zero, split, nonzero semisimple | \((q-1)/2\) | \(q+2\) |
| Trace-zero, nonsplit semisimple | \((q-1)/2\) | \(q\) |
| Nonzero trace and zero determinant | \(q-1\) | \(q\) |
| Nonzero trace and nonzero determinant, nonscalar | \((q-1)^2\) | \(1\) |

The nonsplit row is arithmetically distinctive: its nonzero \(Y\)-orbits are classified by the \(q-1\) nonzero values of the norm \(N_{\mathbb F_{q^2}/\mathbb F_q}\).

## Assumptions and scope

The base field is an arbitrary **finite field of odd characteristic**, including nonprime fields. The algebra is the unital associative algebra with relation \(uv=-vu\). A representation sends \(u\) to \(X\), and \(v\) to \(Y\); its change-of-basis equivalence is simultaneous conjugacy by the same invertible matrix. No semisimplicity, invertibility, or nondegeneracy condition is imposed on the modules. The result does not address characteristic two, larger module dimensions, or the scheme of representations.

## Proof

**Reduction to a rational canonical-form centralizer problem.** Fix the similarity class of \(X\). If \(C(X)\) denotes its invertible centralizer, two compatible matrices \(Y\) give equivalent pairs precisely when they lie in the same \(C(X)\)-conjugacy orbit. The standard complete rational classification of two-by-two matrices gives the seven rows above.

**Zero and scalar classes.** If \(X=0\), the relation imposes no restriction on \(Y\). The number of two-by-two similarity classes is \(q^2+q\): there are \(q\) scalar classes, \(q\) nontrivial Jordan classes, \(q(q-1)/2\) split regular classes, and \((q^2-q)/2\) irreducible quadratic classes. For \(X=aI\) with \(a\ne0\), the relation is \(2aY=0\), hence \(Y=0\); there are \(q-1\) such \(X\)-classes.

**Nonzero nilpotent class.** Fix \(X=\begin{pmatrix}0&1\\0&0\end{pmatrix}\). Direct multiplication shows that every solution is \(Y=\begin{pmatrix}a&b\\0&-a\end{pmatrix}\), with \(a,b\in k\). The invertible centralizer consists of \(sI+tX\), where \(s\in k^*\), \(t\in k\). Its action fixes \(a\) and replaces \(b\) by \(b\pm2at/s\) (the sign is immaterial). For \(a=0\) the parameter \(b\) is invariant, giving \(q\) orbits. For each \(a\ne0\), transitivity on the \(b\)-parameter gives one orbit, yielding \(q+(q-1)=2q-1\).

**Split trace-zero regular classes.** Fix \(X=\operatorname{diag}(a,-a)\) with \(a\in k^*\). Interchanging the two eigenvectors replaces \(a\) by \(-a\); hence there are \((q-1)/2\) distinct \(X\)-classes. The compatible matrices are \(Y=\begin{pmatrix}0&b\\c&0\end{pmatrix}\). Conjugation by the diagonal centralizer rescales \((b,c)\mapsto(rb,r^{-1}c)\). The four orbit types are: the origin; the nonzero \(b\)-axis; the nonzero \(c\)-axis; and one orbit for each prescribed nonzero product \(bc\in k^*\). Thus there are \(3+(q-1)=q+2\) orbits.

**Nonsplit trace-zero regular classes.** Fix an irreducible polynomial \(T^2-d\), with \(d\in k^*\) a nonsquare. There are \((q-1)/2\) such \(d\)'s and exactly one rational similarity class for each polynomial. Identify the underlying two-dimensional space with \(E=\mathbb F_{q^2}\), with \(X\) acting by multiplication by a root \(\theta\) satisfying \(\theta^q=-\theta\). Its anticommuting operators are exactly \(Y_b(v)=b v^q\), where \(b\in E\): every \(k\)-linear map decomposes uniquely as \(v\mapsto av+bv^q\), and anticommutation forces \(a=0\). The invertible centralizer \(E^*\) acts by \(b\mapsto b s^{1-q}\). The homomorphism \(s\mapsto s^{1-q}\) has image the norm-one subgroup of \(E^*\), of order \(q+1\). Hence two nonzero parameters are conjugate if and only if their field norms agree. Since the norm surjects onto \(k^*\), there are exactly \(q-1\) nonzero orbits and the zero orbit, yielding \(q\).

**Nonzero trace cases.** Suppose \(\operatorname{tr}X=t\in k^*\). If \(\det X=0\), then \(X\) is conjugate to \(\operatorname{diag}(t,0)\); the relation forces \(Y=\operatorname{diag}(0,b)\). The diagonal centralizer fixes \(b\), so there are \(q\) orbits for each of the \(q-1\) values of \(t\). If \(\det X\ne0\), then \(Y=0\): over an algebraic closure, the only potentially nonzero matrix entry of \(Y\) could map a \(\lambda\)-eigenspace to a \(-\lambda\)-eigenspace. A nonzero \(Y\) therefore requires either a zero eigenvalue or trace zero; neither occurs. This argument also covers a nontrivial repeated-eigenvalue Jordan block by noting that the spectra of \(X\) and \(-X\) are disjoint, so the Sylvester operator \(Y\mapsto XY+YX\) is invertible. For every pair \((t,d)\in(k^*)^2\), the characteristic polynomial \(T^2-tT+d\) supplies exactly one nonscalar rational similarity class (diagonalizable when roots differ; Jordan when repeated; irreducible when nonsplit). Thus this row contributes \((q-1)^2\) orbits.

**Total.** All cases are disjoint and exhaustive. Summing their contributions gives
\[
(q^2+q)+(q-1)+(2q-1)
+\frac{q-1}{2}(q+2)+\frac{q-1}{2}q
+q(q-1)+(q-1)^2=4q^2+q-2.
\]

## Verification

The independent finite-field enumeration in `verify.py` enumerates all ordered four-entry matrices, tests the anticommutator equation, and constructs simultaneous conjugacy orbits using four standard generators of \(\mathrm{GL}_2(k)\) for the two tested prime fields. It yields \(37\) orbits among \(417\) labeled solutions over \(\mathbb F_3\), and \(103\) orbits among \(4705\) labeled solutions over \(\mathbb F_5\). The exact formula holds for all odd prime powers by the preceding complete algebraic orbit argument; small-field enumeration alone is not its proof. The separate labeled-pair counts are a preexisting result used solely as a consistency check.

To reproduce: run `python3 verify.py` with a standard Python 3 interpreter. It prints `VERIFY_OK` after both exhaustive orbit decompositions.

## Relationship to prior work

Lopes--Lourenço study representations of the quantum plane under the explicit assumption that the deformation parameter is **not** a root of unity, so their isomorphism statements do not apply to the parameter \(-1\). Chen--Wang describe geometric components and the GIT quotient of complex anticommuting varieties. Chen--Lu extend component/GIT-quotient descriptions to quantum planes over algebraically closed fields. Their GIT quotient parametrizes closed orbits, not every rational isomorphism class, including nonsemisimple ones. Huang determines **labeled** finite-field representation counts and explicitly distinguishes the resulting inverse-automorphism-weighted sum from a classification of all module isomorphism classes. The present theorem instead counts **unweighted rational orbits** and exhibits the split/nonsplit field-norm distinction. The already known labeled zero-fiber count is not claimed new. Sharma studies simultaneous similarity of **commuting** matrices, the different relation \(XY=YX\).

## Limitations

No independent mathematical audit has been performed. The result is confined to module dimension two and odd finite-field characteristic. The classification does not determine representation-scheme multiplicities, orbit-closure relations, or higher-dimensional modules. An unlocated specialized classification of root-of-unity quantum-plane modules over arbitrary finite fields could subsume this result; searches and the inspected primary results did not establish such coverage. The exhaustive computational checks use only prime fields of orders three and five; the full odd-prime-power statement rests on the proof.

## References

1. S. A. Lopes and J. N. P. Lourenço, *A multiparameter family of irreducible representations of the quantum plane and of the quantum Weyl algebra*, arXiv:1407.6646 (first public version 2014-07-24); *Portugaliae Mathematica* 72 (2015), 407–419; DOI 10.4171/PM/1973.
2. X. Chen and W. Wang, *Anti-commuting varieties*, arXiv:1805.00378 (2018).
3. X. Chen and M. Lu, *Varieties of modules over the quantum plane*, arXiv:1910.02198 (2019).
4. Y. Huang, *Counting on the variety of modules over the quantum plane*, arXiv:2110.15570 (first version 2021-10-29; revised 2022).
5. U. B. Sharma, *Simultaneous similarity classes of commuting matrices over a finite field*, *Linear Algebra Appl.* 501 (2016), 48–97; DOI 10.1016/j.laa.2016.03.015.
