# Four product-fiber strata in the strictly upper-triangular \(4\times4\) algebra

## Finding
Let \(k=\mathbb F_q\), with \(q\) a prime power, and write \(J=\mathfrak n_4(k)\) for the six-dimensional associative algebra of strictly upper-triangular matrices. For every \(Z\in J\), define the ordered product-fiber size
\[F_q(Z)=\bigl|\{(X,Y)\in J\times J:XY=Z\}\bigr|.\]
All products belong to \(J^2=\operatorname{span}_k\{E_{13},E_{24},E_{14}\}\). Thus \(F_q(Z)=0\) outside this three-dimensional subspace. For \(Z=uE_{13}+vE_{24}+wE_{14}\), introduce the indicator \(\mathbf1_{a=0}\), equal to one when \(a=0\) and to zero otherwise, and \(\mathbf1_{u=v=w=0}\) analogously. Then the *entire* fiber function is
\[
\boxed{F_q(Z)=q^6\left[q(q-1)^2+q^2(q-1)(\mathbf1_{u=0}+\mathbf1_{v=0})+q^4\mathbf1_{u=v=w=0}\right].}
\]
Its four distinct positive values and their numbers of target matrices are:

| Target condition | Number of targets | Ordered factors per target |
|---|---:|---|
| \(Z=0\) | \(1\) | \(q^6[q(q-1)^2+2q^2(q-1)+q^4]\) |
| \(u=v=0,\ w\ne0\) | \(q-1\) | \(q^6[q(q-1)^2+2q^2(q-1)]\) |
| Exactly one of \(u,v\) is nonzero | \(2q(q-1)\) | \(q^6[q(q-1)^2+q^2(q-1)]\) |
| Both \(u,v\) nonzero | \(q(q-1)^2\) | \(q^7(q-1)^2\) |

For the binary field \(q=2\), these sizes are respectively \(1664,640,384,128\); their target multiplicities are \(1,1,4,2\). The weighted sum is \(4096=2^{12}\), the number of ordered pairs in \(J^2\) as a Cartesian set \(J\times J\). Every target in the vector-space square \(J^2\) has a nonempty fiber, a previously known qualitative consequence of the polynomial-image theorem [2]. **The contribution here is the complete quantitative fiber distribution**, not the image statement.

## Assumptions and scope
The base field is any finite field of prime-power cardinality, including characteristic two and nonprime fields. No invertibility, nonzero, nilpotency-index, or rank constraint is imposed on either factor. Products are ordinary ordered associative matrix products; \(F_q(Z)\) counts actual ordered pairs of matrices, not conjugacy classes or orbits. The four target conditions are mutually exclusive and exhaust \(J^2\).

## Proof
Use the elementary-matrix basis ordered as \(E_{12},E_{13},E_{14},E_{23},E_{24},E_{34}\). Write the entries of \(X\) as \(x_{ij}\) and those of \(Y\) as \(y_{ij}\). Direct matrix multiplication gives
\[(XY)_{13}=x_{12}y_{23},\quad (XY)_{24}=x_{23}y_{34},\quad (XY)_{14}=x_{12}y_{24}+x_{13}y_{34}.\]
All other product entries vanish. Six input coordinates \(x_{14},x_{24},x_{34},y_{12},y_{13},y_{14}\) never occur and contribute the factor \(q^6\).

Put \(a=x_{12}\), \(b=x_{13}\), \(c=x_{23}\), \(d=y_{23}\), \(e=y_{24}\), and \(f=y_{34}\). The remaining system for prescribed \((u,v,w)\) is
\[ad=u,\qquad cf=v,\qquad ae+bf=w.\]
Partition all solutions according to the zero/nonzero status of \(a\) and \(f\):

1. If \(a\ne0\) and \(f\ne0\), there are \((q-1)^2\) choices of \((a,f)\), the first two equations uniquely determine \((d,c)\), and the last is one nontrivial linear equation in \((b,e)\) with \(q\) solutions. Contribution \(q(q-1)^2\) for all \((u,v,w)\).
2. If \(a=0\) and \(f\ne0\), necessarily \(u=0\). Once \(f\) is fixed, \(c=v/f\) and \(b=w/f\) are forced, while \(d,e\) are free. Contribution \(q^2(q-1)\mathbf1_{u=0}\).
3. If \(a\ne0\) and \(f=0\), necessarily \(v=0\). Once \(a\) is fixed, \(d=u/a\) and \(e=w/a\) are forced, while \(b,c\) are free. Contribution \(q^2(q-1)\mathbf1_{v=0}\).
4. If \(a=f=0\), all three target coordinates must vanish. Then \(b,c,d,e\) are arbitrary, contributing \(q^4\mathbf1_{u=v=w=0}\).

Adding these disjoint contributions and reinstating the six free matrix coordinates proves the formula, including the cases where \(u\), \(v\), or \(w\) vanish. For \(q\ge2\), the four values are strictly ordered from the first to the fourth row of the table. Counting target coordinates yields multiplicities \(1,q-1,2q(q-1),q(q-1)^2\), which sum to \(q^3\). The target-weighted fiber sum is \(q^{12}\) by partitioning \(J\times J\); it is independently checked by expanding the four expressions.

## Verification
The accompanying self-contained `verify_product_u4.py` implements arithmetic in \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\) and \(\mathbb F_4\), with \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). It exhausts the six effective variables for every target over those four fields, accounts explicitly for six free coordinates, checks the displayed formula at each of the \(q^3\) targets, and checks the total \(q^{12}\). Separately, it multiplies all \(4096\) ordered pairs of full \(4\times4\) matrices over \(\mathbb F_2\) and all \(531441\) ordered pairs over \(\mathbb F_3\), agreeing with the independent effective-coordinate enumeration. Run `python verify_product_u4.py`; the success marker is `VERIFY_OK_PRODUCT_U4`. These checks are finite confirmations; the four-case proof establishes the arbitrary-prime-power theorem.

## Relationship to prior work
The strictly upper-triangular algebra is the canonical maximal-dimensional linear nilpotent matrix space by the equality theorem discussed by de Seguins Pazzis [1, Theorems 1–2], fixing the natural object. Fagundes [2, Theorem 3] establishes that the image of any nonidentity multilinear polynomial on strictly upper-triangular matrices is the appropriate higher-radical subspace; specializing to the word \(XY\) establishes \(XY(J,J)=J^2\) but does **not** assign multiplicities to individual prescribed products. The present claim refines this image classification to all finite-field fiber counts. Additive commutator fibers for \([X,Y]=XY-YX\) are different invariants: knowing the distribution of differences does not determine the separate ordered product-fiber function. Related finite-field matrix factorization counts involving nonnilpotent idempotent or involutory factors likewise concern different domains and do not imply this calculation.

## Limitations
The formula concerns exactly the square of the strictly upper-triangular \(4\times4\) matrix algebra, not arbitrary \(n\), other polynomial words, or products of three or more factors. It does not claim a new image theorem or a new characterization of maximal nilpotent subspaces. Priority remains subject to undiscovered equivalent historical finite-semigroup enumerations. No independent mathematical audit is asserted.

## References
[1] Clément de Seguins Pazzis, *On Gerstenhaber's theorem for spaces of nilpotent matrices over a skew field*, arXiv:1210.4951v1 (first publicly posted 2012-10-17); *Linear Algebra and its Applications* 438 (2013), 4426–4438. https://arxiv.org/abs/1210.4951

[2] Pedro S. Fagundes, *The images of multilinear polynomials on strictly upper triangular matrices*, arXiv:1807.09136v1 (first publicly posted 2018-07-24); *Linear Algebra and its Applications* 563 (2019), 287–301. https://arxiv.org/pdf/1807.09136
