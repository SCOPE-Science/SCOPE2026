# Arithmetic stratification and exceptional orbits of the Fano cubic net

## Finding
Let \(q=2^m\) for an integer \(m\ge1\). For the linear net of cubics passing through all seven points of \(\mathbf P^2(\mathbf F_2)\), there are precisely \(7\) reduced unions of three concurrent \(\mathbf F_2\)-lines, \(7(q-2)\) unions of a line and a smooth conic tangent to it, and \((q-2)(q-4)\) geometrically integral cuspidal cubics. Their respective rational point counts are \(3q+1\), \(2q+1\), and \(q+1\).

On the cuspidal locus the \(168\)-element group \(G=\operatorname{PGL}_3(\mathbf F_2)\) acts with a single exceptional orbit of size \(24\) if \(3\mid m\), and none otherwise. Every other orbit has size \(168\). Consequently the precise numbers of projective orbits are
\[
\begin{cases}
(q-2)(q-4)/168,&3\nmid m,\\
1+((q-2)(q-4)-24)/168,&3\mid m.
\end{cases}
\]
The known existence and geometric construction of cuspidal cubics in this net are not asserted to be new; the arithmetic classification and stabilizer formula are the contribution assessed here.

## Assumptions and scope
Use the algebraically closed geometric classification over characteristic two and count \(\mathbf F_q\)-rational projective equations (scalar multiples identified), not abstract curve isomorphism classes. Let
\[
F_{a,b,c}=aXY(X+Y)+bYZ(Y+Z)+cZX(Z+X),\qquad [a:b:c]\in\mathbf P^2(\mathbf F_q).
\]
Evaluation on \(\mathbf P^2(\mathbf F_2)\) has rank seven among degree-three forms, so these three cubics form a basis of the kernel. Every parameter is nonzero projectively. The natural group is the automorphism group of the seven marked base points, not the whole \(\operatorname{PGL}_3(\mathbf F_q)\).

## Proof
**1. The unique singularity.** In characteristic two, derivatives are
\[
\partial_XF=aY^2+cZ^2,\quad \partial_YF=aX^2+bZ^2,\quad \partial_ZF=bY^2+cX^2.
\]
Because \(\mathbf F_q\) is perfect, all three vanish at exactly one geometric projective point \(P=[\sqrt b:\sqrt c:\sqrt a]\). Substitution makes \(F(P)=0\). Expanding a sum of terms of the form \(X^2Y\) around \(P\), its quadratic homogeneous part has no mixed terms; the tangent cone is a repeated line whenever the cubic is geometrically integral. Thus a geometrically integral member has a unique rational cusp and its smooth normalization is \(\mathbf P^1\).

**2. Reducible locus.** A reducible plane cubic has a geometric line component. If that line is not defined over \(\mathbf F_2\), it contains at most one of the seven \(\mathbf F_2\)-points, so its residual conic contains at least six. Among any six Fano points three are collinear, forcing that conic to contain a line defined over \(\mathbf F_2\) by Bézout. Therefore every reducible member has an \(\mathbf F_2\)-line factor. For each of the seven Fano lines \(L\), the condition \(L\mid F_{a,b,c}\) is a line in coefficient-parameter space, and these seven parameter lines are exactly
\[
a=0,\ b=0,\ c=0,\ a+b=0,\ a+c=0,\ b+c=0,\ a+b+c=0.
\]
They form the Fano incidence arrangement. Exactly seven coefficient points lie on three lines, exactly \(7(q-2)\) lie on one, and the remaining \((q-2)(q-4)\) lie on none. A three-line parameter yields three distinct \(\mathbf F_2\)-line factors concurrent at \(P\). In the one-line case the residual conic cannot split: four base points outside the line force any split residual to have another \(\mathbf F_2\)-line factor, contrary to uniqueness. It is therefore geometrically smooth and meets the line at the unique singular point with multiplicity two. The no-line case is geometrically integral and cuspidal by the preceding paragraph.

**3. Rational point counts.** A rational projective line and a smooth rational conic each have \(q+1\) rational points and share exactly the rational tangent point, giving \(2q+1\). Three concurrent rational lines have \(3q+1\) rational points. For the integral cuspidal cubic the normalization \(\mathbf P^1\to C\) induces a bijection on rational points, since the unique rational cusp is geometrically unibranch, giving \(q+1\).

**4. Exceptional orbits.** The map \([a:b:c]\mapsto[\sqrt b:\sqrt c:\sqrt a]\) identifies the cuspidal parameter locus with the complement of the seven \(\mathbf F_2\)-lines in \(\mathbf P^2(\mathbf F_q)\), and intertwines the marked-plane symmetry action (up to the indicated cyclic coordinate permutation). The group \(G\) has order \(168\) and element orders \(1,2,3,4,7\). Elements of orders \(2\) or \(4\) have projective fixed points only in an \(\mathbf F_2\)-defined proper linear subspace. Every fixed point of an order-three element is defined over \(\mathbf F_4\), and every point of \(\mathbf P^2(\mathbf F_4)\) lies on at least one Fano line. Hence only elements of order seven can fix cuspidal parameters. Such an element has irreducible cubic characteristic polynomial over \(\mathbf F_2\) and three eigenpoints over \(\mathbf F_8\) outside the arrangement. These points are rational over \(\mathbf F_q\) exactly when \(3\mid m\). There are eight Sylow-seven subgroups in \(G\); their \(8\cdot3=24\) eigenpoints are distinct and form one orbit of size \(24\). Each has cyclic point stabilizer of order \(7\); all other points have trivial stabilizer. Orbit-stabilizer gives the formula above.

## Verification
The attached independent-of-literature finite-field checker enumerates the projective parameter plane, the seven incidence lines, the \(168\) binary projective transformations, and all cuspidal orbits for \(q\in\{2,4,8,16,32,64\}\). It checks the full formula and obtains cuspidal orbit sizes \(\varnothing,\varnothing,\{24:1\},\{168:1\},\{168:5\},\{24:1,168:22\}\), respectively. As an additional direct test, counting zeros of a representative cuspidal equation over \(\mathbf F_8\) and \(\mathbf F_{16}\) gives \(9\) and \(17\) rational curve points, as predicted. These finite tests support but do not replace the all-\(m\) proof.

Run `python3 checks/fano_cubic_check.py` with Python 3 (standard library only), and compare its output to `checks/expected_counts.txt`.

## Relationship to prior work
Akesseh's 2017 dissertation establishes the Fano-plane exceptional interpolation and links it with quasi-elliptic fibrations. The 2018 work of Di Marca--Malara--Oneto develops the theory of unexpected curves and line arrangements in characteristic zero. Kettinger's 2025 classification directly supplies the characteristic-two unexpected-cubic geometric context and the Fano net. The present result does not re-claim these constructions; it determines their finite-extension arithmetic strata, point spectra, and the unique cyclic-seven symmetry exception. Published records searched by statement, aliases, and parameters did not reveal this complete quantitative theorem; that is not an assertion of exhaustive publication priority.

## Limitations
The orbit classification uses automorphisms of the fixed seven-point Fano configuration. It is not a classification up to \(\operatorname{PGL}_3(\mathbf F_q)\) or up to abstract curve isomorphism. The theorem requires \(q\) to be a power of two. The earliest known background dissertation has only month-granularity dating in its repository, and its complete file could not be accessed, leaving publication-priority uncertainty. No independent external review has been conducted.

## References
1. S. Akesseh, *Ideal Containments under Flat Extensions and Interpolation on Linear Systems in P²* (dissertation, August 2017), https://digitalcommons.unl.edu/mathstudent/80/.
2. M. Di Marca, G. Malara, A. Oneto, *Unexpected curves arising from special line arrangements* (first public 2018-04-08), https://arxiv.org/abs/1804.02730.
3. J. Kettinger, *The classification of quasi-elliptic fibrations and unexpected plane cubics in characteristics 2 and 3* (first public 2025-10-07), https://arxiv.org/abs/2510.06365.
