# The modular \(\delta\)-derivation spectrum of the five-dimensional special-affine Lie algebra

## Finding

Let \(k\) be any field with \(\operatorname{char}(k)\ne2\), let \(L=\mathfrak{sl}_2(k)\ltimes k^2\) with the natural module, and write \(\operatorname{Der}_\delta(L)\) for all linear maps \(D:L\to L\) satisfying
\[
D([a,b])=\delta\bigl([D(a),b]+[a,D(b)]\bigr)\qquad(a,b\in L).
\]
For every \(\delta\in k\), its dimension is exactly
\[
\boxed{\begin{aligned}
\dim_k\operatorname{Der}_\delta(L)
={}&4\mathbf1_{\{\delta=1\}}
+2\mathbf1_{\{(\delta-1)(\delta+2)=0\}}\\
&+2\mathbf1_{\{\delta=-2\}}
+\mathbf1_{\{2\delta=1\}}.
\end{aligned}}
\]
The summands are not presumed disjoint: the parameter values can collide in small positive characteristics. In particular, when the characteristic is neither \(3\) nor \(5\), the only nonzero dimensions are \(6\) at \(\delta=1\), \(4\) at \(\delta=-2\), and \(1\) at \(\delta=1/2\); in characteristic \(3\), they are \(8\) at \(\delta=1\) and \(1\) at \(\delta=-1\); in characteristic \(5\), they are \(6\) at \(\delta=1\) and \(5\) at \(\delta=-2=1/2\). All other values have dimension zero. When \(k=\mathbb F_q\), the corresponding space contains exactly \(q^{\dim_k\operatorname{Der}_\delta(L)}\) linear maps.

## Assumptions and scope

The ordered basis is \((h,e,f,u,v)\), with nonzero fundamental brackets
\[
[h,e]=2e,\quad[h,f]=-2f,\quad[e,f]=h,\quad
[h,u]=u,\quad[h,v]=-v,\quad[e,v]=u,\quad[f,u]=v.
\]
Other brackets are determined by skew-symmetry and bilinearity, with \([u,v]=0\). The theorem covers arbitrary fields, including nonperfect fields and all odd positive characteristics; no assumption of algebraic closedness is used. It concerns ordinary (even) linear \(\delta\)-derivations, not Lie-superalgebra derivations.

## Proof

1. **Build the complete polynomial system.** Write \(D(b_j)=\sum_a d_{aj}b_a\) for the five basis vectors, and \([b_i,b_j]=\sum_t c_{ij}^{t}b_t\). The defining equations for the ten pairs \(i<j\), in each of the five output coordinates \(k\), have coefficient in column \((a,b)\)
\[
M_{(i,j,k),(a,b)}(\delta)
=\mathbf1_{\{k=a\}}c_{ij}^{b}
-\delta\mathbf1_{\{b=i\}}c_{aj}^{k}
-\delta\mathbf1_{\{b=j\}}c_{ia}^{k}.
\]
This gives a \(50\times25\) matrix. No equations are omitted: because the bracket is alternating, the ten distinct basis pairs suffice in every characteristic other than \(2\).

2. **Integral unit-pivot elimination.** Elementary row operations and unit (\(\pm1\)) pivots eliminate fourteen variables, without ever dividing by a characteristic-sensitive scalar. With column ordering \((a,b)\mapsto5a+b\), the eleven free-column indices, starting from zero, are
\[
(1,2,6,7,11,12,16,17,21,22,24).
\]
Write their coefficients as \(t_1,\ldots,t_{11}\). The residual nineteen relations, after removing redundant multiples and dividing only by the invertible scalar \(2\), are equivalent to
\[
\begin{gathered}
(\delta-1)t_1=(\delta-1)t_2=0,\qquad t_4=t_5=0,\\
(\delta-1)(\delta+2)t_7=(\delta-1)(\delta+2)t_{10}=0,\\
(\delta+2)t_8=(\delta+2)t_9=0
\end{gathered}
\]
and the following five equations, on \(a=t_3\), \(b=t_6\), \(c=t_{11}\):
\[
\begin{aligned}
(\delta^2+\delta-1)a+\delta^2b&=0,\\
\delta^2a+(\delta^2+\delta-1)b&=0,\\
-\delta(2\delta-1)a-\delta^2b-\delta(\delta-1)c&=0,\\
\delta^2(a+b)+(\delta-1)c&=0,\\
-\delta^2a-\delta b-(\delta-1)(\delta+1)c&=0.
\end{aligned}
\]
For complete reproducibility, `verify.py` constructs the \(50\times25\) matrix from the displayed brackets, performs the unit-pivot elimination, and compares **all nineteen residual rows, entry by entry**, against a separately specified polynomial matrix. Thus this reduction is an explicit exact finite algebraic certificate, not a numerical-rank inference. In particular it is valid after reduction in every odd characteristic.

3. **Solve the residual system.** The first eight free variables contribute \(2\), \(2\), and \(2\) dimensions, respectively, exactly at \(\delta=1\), \((\delta-1)(\delta+2)=0\), and \(\delta=-2\). For the last three unknowns, subtraction of the first two equations gives \((\delta-1)(a-b)=0\). If \(\delta=1\), all five equations reduce to \(a+b=0\), with \(c\) free: dimension \(2\). If \(\delta\ne1\), then \(a=b\) and the first equation reduces to \((\delta+1)(2\delta-1)a=0\). If \(\delta\ne-1,1/2\), the fourth equation gives \(c=0\). At \(\delta=-1\ne1/2\), the third and fourth equations force \(6a=0\), whence \(a=0\) (the only odd characteristic dividing \(6\) is \(3\), where \(-1=1/2\)). At \(\delta=1/2\ne1\), the five equations give \(a=b=c\), dimension \(1\). This proves the stated formula without an assumption on \(k\) beyond \(2\ne0\).

4. **Characteristic collisions.** The values \(-2\) and \(1\) coincide only in characteristic \(3\); the values \(-2\) and \(1/2\) coincide only in characteristic \(5\). The exact dimensions therefore jump as stated. No finite sampling is used in this proof.

## Verification

Run `python verify.py` with Python 3 and SymPy. The program constructs the defining matrix, independently checks the nineteen-row polynomial reduction, and evaluates all possible \(\delta\)-values in prime fields of characteristics \(3,5,7,11,13,17\), together with the exceptional and generic rational values. It ends with `VERIFY_OK`. The recorded output is in `verify_output.txt`. These computations corroborate the universal symbolic proof, rather than replacing it.

## Relationship to prior work

Kaygorodov, Khudoyberdiyev and Shermatova (submitted 2026-10-16) classify homogeneous derivations and \(\delta\)-derivations for the infinite-dimensional Block Lie superalgebras \(S(q)\) over \(\mathbb C\). Those are distinct objects; the work motivates a characteristic-sensitive classification for a small ordinary semidirect Lie algebra. Nuratdinov and G'aybullaev (submitted 2026-10-27) explicitly compute the four-dimensional \((-2)\)-derivation space of \(\mathfrak{sl}_2(\mathbb C)\ltimes\mathbb C^2\). Their published complex result agrees with the characteristic-zero specialization here and is **not claimed as new**. Their hypotheses do not cover characteristic \(3\) or \(5\), or arbitrary odd-characteristic fields; the full modular spectrum and the two collision dimensions are the distinct results here.

## Limitations

No statement is made for characteristic \(2\), for higher-dimensional special-affine Lie algebras, or for Lie-superalgebra homogeneous maps. Historical originality is subject to comparison with any earlier general modular \(\delta\)-derivation classification not retrieved. The displayed rank data on finitely many fields do not themselves establish the theorem; the unit-pivot symbolic elimination and kernel calculation do. Independent review has not been performed.

## References

1. I. Kaygorodov, A. Khudoyberdiyev, Z. Shermatova, *Derivations and quasi-derivations of Block Lie superalgebras \(S(q)\)*, arXiv:2610.23150v1, first public 2026-10-16, https://arxiv.org/abs/2610.23150.
2. K. Nuratdinov, R. G'aybullaev, *On \(\delta\)-derivations of \(\mathfrak{saff}_{n+1}\)*, arXiv:2610.37027v1, first public 2026-10-27, https://arxiv.org/abs/2610.37027.
