# Conjugacy-class spectrum of units centralizing a subregular nilpotent matrix

## Finding

Let \(q\) be any prime power, let \(m\ge 2\), put \(k=\mathbb F_q\), and let \(N_m=J_m(0)\oplus J_1(0)\) be a nilpotent matrix of type \((m,1)\). Let \(G_m=C_{\operatorname{GL}_{m+1}(k)}(N_m)\) be its invertible matrix centralizer. Then
\[
|G_m|=(q-1)^2q^{m+1},\qquad
k(G_m)=(q-1)(q^2+1)q^{m-2},
\]
where \(k(G_m)\) is the number of conjugacy classes **within** \(G_m\). The complete element and conjugacy-class size spectrum is as follows:

| Class size | Elements | Classes |
| --- | ---: | ---: |
| \(1\) | \((q-1)q^{m-1}\) | \((q-1)q^{m-1}\) |
| \(q(q-1)\) | \((q-1)q^{m-1}(q^2-1)\) | \(q^{m-2}(q^2-1)\) |
| \(q^2\) | \((q-1)(q-2)q^{m+1}\) | \((q-1)(q-2)q^{m-1}\) |

The third row is empty when \(q=2\); otherwise all three class sizes occur. In particular, the commuting probability of two independently uniformly chosen elements of \(G_m\) is
\[
\boxed{\operatorname{cp}(G_m)=\frac{q^2+1}{q^3(q-1)}},
\]
**independent of \(m\)**, even though \(|G_m|\) and its class multiplicities grow with \(m\). For \(q=2\) the probability is \(5/8\) at every \(m\ge2\).

## Assumptions and scope

All groups are finite. The nilpotent Jordan block \(J_m(0)\) has exactly one block of size \(m\), and \(J_1(0)\) is the zero \(1\times1\) block. This is an **internal** conjugacy-class count for its unit centralizer, not a count of ordinary similarity classes in the ambient general linear group. No restriction on characteristic is imposed. The case \(m=1\), when the centralizer is the full \(\operatorname{GL}_2(k)\), is excluded.

## Proof

Identify \(k^{m+1}\) with the \(k[t]\)-module \(M=R\oplus k\), where \(R=k[t]/(t^m)\) and \(t\) annihilates the second summand. Multiplication by \(t\) on \(M\) is conjugate to \(N_m\). The endomorphism algebra \(A=\operatorname{End}_{k[t]}(M)\) is therefore the full matrix centralizer. Any \(X\in A\) is uniquely specified by
\[
X=(f,u,v,a),\quad f\in R,\quad u,v,a\in k,
\]
where the four block maps are \(R\to R\), multiplication by \(f\); \(k\to R\), sending \(1\mapsto u t^{m-1}\); \(R\to k\), sending \(p(t)\mapsto v p(0)\); and \(k\to k\), multiplication by \(a\). Write \(f_0=f(0)\). The matrix of this operator in the basis \(1,t,\ldots,t^{m-1}\), followed by a basis of \(k\), has determinant \(f_0^m a\): the off-diagonal blocks cannot alter the determinant since the second-to-first map lands in the \(t^{m-1}\) socle and its subsequent first-to-second map vanishes for \(m\ge2\). Hence
\[
X\in G_m\iff f_0\ne0\ \text{and}\ a\ne0,
\]
and counting \(m-1\) remaining coefficients of \(f\) and two free off-diagonal scalars gives \(|G_m|=(q-1)^2q^{m+1}\).

Let \(Y=(g,U,V,b)\), with \(g_0=g(0)\). Computing both compositions, and using \(t^{m-1}h(t)=h(0)t^{m-1}\) as well as \(\operatorname{ev}_0(t^{m-1})=0\), shows that \(XY=YX\) is **equivalent**, with no omitted equations, to
\[
 uV-Uv=0,\quad (f_0-a)U-(g_0-b)u=0,\quad
 v(g_0-b)-V(f_0-a)=0.
\]
With \(h=f_0-a\) and \(h'=g_0-b\), these are precisely the three minors of the two-by-three matrix whose rows are \((h,u,v)\) and \((h',U,V)\). Thus for a given \(X\), its centralizer in \(G_m\) consists of precisely those \(Y\in G_m\) whose three-vector lies in the one-dimensional span of \((h,u,v)\), unless that vector is zero, in which case all \(Y\) commute.

For fixed \(h'\in k\), the number of ordered nonzero scalars \((g_0,b)\in(k^\times)^2\) satisfying \(g_0-b=h'\) is \(q-1\) if \(h'=0\), and \(q-2\) otherwise. In every case the other \(m-1\) coefficients of \(g\) are freely chosen, contributing \(q^{m-1}\). Accordingly:

- When \((h,u,v)=(0,0,0)\), all \(|G_m|\) choices commute. Exactly \((q-1)q^{m-1}\) elements \(X\) belong to this stratum.
- When \(h=0\) but \((u,v)\ne(0,0)\), the commuting \(Y\) have \(h'=0\), and their off-diagonal coordinates are the \(q\) scalar multiples of \((u,v)\). Hence \(|C_{G_m}(X)|=q^m(q-1)\). There are \((q-1)q^{m-1}(q^2-1)\) such \(X\).
- When \(h\ne0\), the commuting three-vectors are \(\lambda(h,u,v)\) for \(\lambda\in k\). There is one \(\lambda=0\) choice with \(q-1\) possibilities for \((g_0,b)\), plus \(q-1\) nonzero \(\lambda\), each with \(q-2\) possibilities. Thus \(|C_{G_m}(X)|=(q-1)^2q^{m-1}\). There are \((q-1)(q-2)q^{m+1}\) such \(X\), and none in this stratum when \(q=2\).

The conjugacy class of \(X\) in \(G_m\) has cardinality \(|G_m|/|C_{G_m}(X)|\), yielding exactly \(1\), \(q(q-1)\), and \(q^2\) in the three respective strata. Dividing each element multiplicity by its class size proves the displayed table and, after summation, \(k(G_m)=(q-1)(q^2+1)q^{m-2}\). Finally, Burnside's lemma gives
\[
\#\{(X,Y)\in G_m^2:XY=YX\}=|G_m|\,k(G_m),
\]
so division by \(|G_m|^2\) yields the claimed commuting probability. Every step applies to all prime powers \(q\), including characteristic two.

## Verification

The standalone Python file `verify_subregular_unit_centralizers.py` enumerates all units and all commuting partners for \((q,m)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2)\). It supports the extension field \(\mathbb F_4\) via \(\mathbb F_2[z]/(z^2+z+1)\). It independently constructs full matrices and compares literal matrix commutation with the three-minor criterion for \((2,2),(2,3),(3,2)\). All seven configurations passed; for \((q,m)=(3,2)\), in particular, the verifier obtains \(|G_m|=108\), \(20\) conjugacy classes, and \(2160\) commuting ordered pairs. Reproduce from the package by executing `python3 verify_subregular_unit_centralizers.py` with Python 3. The finite checks corroborate the universal algebraic proof; they are not a proof of all \(m\) and \(q\).

## Relationship to prior work

Britnell and Wildon (2010) establish fundamental similarity-type and matrix-centralizer compatibility results, including conditions on determinants of centralizer elements and commuting nilpotent similarity classes. Their theorems address whether prescribed ambient similarity classes can contain commuting representatives rather than the internal conjugacy-class-size spectrum of the invertible centralizer studied here.

Sharma (first public version 2014; 2016 publication), especially Lemmas 4.2 and 5.10, computes orbit branching of **all matrices** in centralizers for the \((2,1)\) and \((3,1)\) Jordan types. The small \(m=2,3\) specializations have antecedents in that branching analysis and are not separately advanced as new. The present statement concerns the full **unit-only class-size distribution for all \(m\ge2\)** and its rank-uniform commuting-probability corollary. Those all-length assertions are not present in the inspected portions of Sharma's paper. The broader algebraic study of commuting varieties by Ngo concerns additive/Lie centralizer loci, not immediately the conjugacy-class spectrum of the group of invertible elements. Equivalently phrased older results could subsume the count, a residual bibliographic risk.

## Limitations

The finding is restricted to the subregular Jordan partition \((m,1)\) and internal conjugation by invertible elements of its own centralizer. It does not classify all centralizer isomorphism types, general two-part partitions, algebraic-group orbit geometry, or ambient simultaneous similarity classes. Completeness of the historical bibliography and independently performed mathematical validation are not established.

## References

1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, first public arXiv version 6 January 2010, arXiv:1001.0811.
2. U. B. Sharma, *Simultaneous Similarity Classes of Commuting matrices over a finite field*, arXiv:1409.2698, first public 7 September 2014; *Linear Algebra and its Applications* **501** (2016), 48–97. In particular Lemmas 4.2 and 5.10.
3. N. V. Ngo, *Mixed Commuting Varieties over simple Lie algebras*, arXiv:1301.2712 (2013), as surrounding commuting-variety literature.
