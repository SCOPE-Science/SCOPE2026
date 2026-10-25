# The minimal genus-one multisection index of \(\langle32\rangle\oplus D_4(-1)\)

## Finding

Let
\[
L=\langle32\rangle\oplus D_4(-1),\qquad D_4=\{(y_1,y_2,y_3,y_4)\in\mathbb Z^4:\;y_1+y_2+y_3+y_4\equiv0\pmod2\},
\]
where the \(D_4\) form is the negative of the standard Euclidean form. For every primitive isotropic vector \(v\in L\), its divisibility
\[
\operatorname{div}_L(v)=\gcd\{(v,w):w\in L\}
\]
is a multiple of \(4\). The vector \(v_0=(1;4,4,0,0)\) is primitive isotropic and has divisibility exactly \(4\). Therefore any complex K3 surface \(S\) with \(\operatorname{NS}(S)\cong L\) has minimum genus-one multisection index exactly \(4\), and no genus-one fibration on \(S\) has index \(1\), \(2\), or \(3\).

## Assumptions and scope

The lattice is the rank-five even hyperbolic lattice \(\langle 2^5\rangle\oplus D_4\) used as an example in the recent study of K3 automorphism groups; here \(\langle 2^5\rangle=\langle32\rangle\) and \(D_4\) is negative definite. The statement is conditional on a complex K3 surface having this Néron–Severi lattice, whose occurrence is cited in the literature. A genus-one fibration has a primitive isotropic fiber class. Its multisection index is the positive generator of the ideal of intersections of that class with \(\operatorname{NS}(S)\), equivalently its lattice divisibility.

## Proof

Write an isotropic vector as \(v=(a;y_1,y_2,y_3,y_4)\), with \(a\in\mathbb Z\) and \(y\in D_4\). The equation \((v,v)=0\) is
\[
 y_1^2+y_2^2+y_3^2+y_4^2=32a^2.
\]
The right side is divisible by \(8\). Every integer square is congruent to \(0\), \(1\), or \(4\) modulo \(8\). If exactly \(r\) of the four coordinates are odd, their squares contribute \(r\) modulo \(8\); each even coordinate contributes either \(0\) or \(4\). For \(r=1,2,3\), adding any number of \(4\)'s cannot give \(0\) modulo \(8\); for \(r=4\), the sum is \(4\) modulo \(8\). Thus all \(y_i\) are even. Write \(y_i=2z_i\). Then \(\sum_i z_i^2=8a^2\), and the same residue argument shows that every \(z_i\) is even. Hence each \(y_i\) is divisible by \(4\).

Let \(e=(1;0,0,0,0)\) be the generator of the rank-one summand. We have \((v,e)=32a\in4\mathbb Z\). For every \(x\in D_4\), we also have \((v,x)=-\sum_i y_ix_i\in4\mathbb Z\). Therefore \(\operatorname{div}_L(v)\) is divisible by \(4\).

Now \(v_0=(1;4,4,0,0)\) lies in \(L\), since its last four coordinates sum to an even integer, and
\[
(v_0,v_0)=32-4^2-4^2=0.
\]
It is primitive because its first coordinate is \(1\). Its pairing with every vector in the \(D_4(-1)\) summand is divisible by \(4\), and the vector \(x=(1,0,1,0)\in D_4\) gives \((v_0,x)=-4\). Its pairing with \(e\) is \(32\). The gcd of all pairings is therefore exactly \(4\).

For a K3 surface, a primitive isotropic class can be moved to a nef isotropic class by the usual root-reflection/chamber argument, without changing divisibility; a nef primitive isotropic class defines a genus-one fibration. Since the multisection index equals the divisibility of the fiber class, the lower bound and the exhibited value give minimum index \(4\).

## Verification

The argument is an exact congruence proof in the stated lattice; it uses no numerical search or finite enumeration. The witness \(v_0\) is checked directly for membership, isotropy, primitivity, and divisibility. The K3-geometric step uses the standard correspondence between nef primitive isotropic classes and genus-one fibrations, together with the identification of multisection index and fiber-class divisibility. This does not classify all fibrations or their singular fibers.

## Relationship to prior work

Fujiwara, Oguiso, and Yu use \(\langle 2^5\rangle\oplus D_4\) as a rank-five K3 Néron–Severi lattice with maximal Mordell–Weil rank zero and infinite automorphism group, in discussing a limitation of a virtual-cohomological-dimension conjecture. Their stated example does not compute the divisibility of primitive isotropic classes or the minimum multisection index. The present claim supplies that specific lattice invariant by an explicit congruence argument. General references on elliptic K3 surfaces define multisection index through intersections with the fiber class; they do not, in the inspected material, supply this calculation for the rank-five lattice above.

## Limitations

The result gives the minimum multisection index, not a classification of all primitive isotropic vectors up to lattice isometry, all genus-one fibrations, their Kodaira fiber configurations, or their Jacobian surfaces. The literature search did not establish absolute novelty; an older detailed classification of fibrations on this exact lattice remains a residual possibility. No independent mathematical audit has been performed.

## References

1. K. Fujiwara, K. Oguiso, and X. Yu, “On K3 surfaces with hyperbolic automorphism groups,” arXiv:2507.13726, first posted 18 July 2025; published version, *Journal für die reine und angewandte Mathematik*, DOI: 10.1515/crelle-2026-0036. In particular, Remark 1.5(4) gives the lattice \(\langle 2^5\rangle\oplus D_4\) as an example with zero maximal Mordell–Weil rank and infinite automorphism group.
2. R. Meinsma and E. Shinder, “Derived equivalence for elliptic K3 surfaces and Jacobians,” *International Mathematics Research Notices* (2024), DOI: 10.1093/imrn/rnae061. Section 3.1 defines the multisection index by intersections with the fiber class.
