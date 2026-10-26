# All-squarefree binary-quartic pencils over \(\mathbf F_5\): 47 source-coordinate orbits

## Finding
Let \(k=\mathbf F_5\) and \(V=H^0(\mathbf P^1_k,\mathcal O(4))\). A *squarefree pencil* is a two-dimensional \(k\)-vector subspace \(W\subset V\) such that each of its six nonzero projective \(k\)-members is a binary quartic with four distinct geometric roots on \(\mathbf P^1\).

Among the \(20\,306\) pencils in \(\operatorname{Gr}(2,5)(k)\), exactly \(3\,820\) are squarefree. Under the full source-coordinate action \(\operatorname{PGL}_2(k)\) they form precisely \(47\) orbits. The orbit-size multiplicities are

| Orbit size | Number of orbits | Number of pencils |
|---:|---:|---:|
| 10 | 2 | 20 |
| 20 | 1 | 20 |
| 40 | 3 | 120 |
| 60 | 21 | 1260 |
| 120 | 20 | 2400 |
| Total | 47 | 3820 |

Let \(B_W\) be the common zero divisor of any basis of \(W\), interpreted as the scheme-theoretic base divisor on \(\mathbf P^1\). Its degree has the complete frequency distribution

| Degree of \(B_W\) | Pencil count |
|---:|---:|
| 0 | 3710 |
| 2 | 70 |
| 3 | 40 |

In particular, \(3\,710\) pencils are basepoint-free. Such a pencil defines a degree-four separable morphism \(\mathbf P^1_k\to\mathbf P^1_k\) with geometrically reduced fibres over all six rational target points. No squarefree pencil has a rational base point. Furthermore, the six rational members realize exactly \(14\) possible multisets of Frobenius root-degree partitions; the full list and multiplicities appear in `data/census_catalogue.json`.

Exactly \(540\) of the \(3\,820\) pencils possess a rational member split into four distinct \(k\)-linear factors, and no pencil has two such members.

## Assumptions and scope
All arithmetic is over the prime field \(k=\mathbf F_5\). Write a quartic as \(aX^4+bX^3Z+cX^2Z^2+dXZ^3+eZ^4\), represented by the coefficient vector \((a,b,c,d,e)\in k^5\). Projective members are taken modulo \(k^\times\), and only *source* substitutions \((X,Z)\mapsto(aX+bZ,cX+dZ)\) are used for the orbit classification. Basis changes within a pencil identify the same subspace automatically. No quotient by arbitrary \(\operatorname{GL}_5(k)\) is asserted.

Every squarefree quartic defines the branch divisor of a geometrically smooth genus-one double cover of \(\mathbf P^1\) in characteristic five. The counts concern pencils of branch divisors, not isomorphism classes of elliptic curves or degree-four maps with independently marked target coordinates. For a basepoint-free pencil the target coordinate is determined only up to \(\operatorname{PGL}_2(k)\).

## Proof
**1. Exact squarefreeness predicate.** For \(F=aX^4+bX^3Z+cX^2Z^2+dXZ^3+eZ^4\) define
\[ I(F)=12ae-3bd+c^2,\qquad J(F)=72ace+9bcd-27ad^2-27eb^2-2c^3. \]
For binary quartics, \(27\operatorname{Disc}(F)=4I(F)^3-J(F)^2\). Since \(27\) is invertible in characteristic five, \(F\) is geometrically squarefree precisely when \(4I(F)^3-J(F)^2\ne0\). This includes the root at infinity. Independently, a repeated root of a degree-four form has degree at most two over \(k\), so affine polynomial gcd tests plus the infinity condition provide another exact squarefreeness test. Both count \(600\) squarefree projective quartics among the \(781=(5^5-1)/4\) projective forms.

**2. Exhaustion of pencil space.** Every two-dimensional subspace of \(k^5\) has a unique reduced-row-echelon \(2\times5\) basis. The ten possible pivot pairs \(0\le i<j\le4\) and all assignments to free entries enumerate exactly
\[ {5\brack2}_5=\frac{(5^5-1)(5^5-5)}{(5^2-1)(5^2-5)}=20\,306 \]
pencils, each exactly once. A pencil with basis \(f,g\) has six projective members \(g,f,f+g,f+2g,f+3g,f+4g\), and the six discriminants are computed exactly in \(k\). Exactly \(3\,820\) unique RREF pencils pass all six tests. A second enumerator instead constructs pencils from unordered pairs of the \(781\) projective forms, canonically identifies their six members, and returns the same total. The implementations use different forms of the squarefreeness test (quartic invariant versus polynomial gcd).

**3. Orbit completeness.** Enumerate the \(120=5(5^2-1)\) elements of \(\operatorname{PGL}_2(k)\) as scalar-normalized invertible \(2\times2\) matrices. Their induced degree-four substitutions give linear actions on \(k^5\). For each unvisited RREF pencil, form its full orbit, row-reduce every image, and remove these images from the remaining exact set. The resulting \(47\) disjoint orbits have sizes \(10,20,40,60,120\) with multiplicities \(2,1,3,21,20\), whose weighted sum is \(3\,820\). Each orbit representative and stabilizer order is in `data/census_catalogue.json`. Because both the initial RREF enumeration and all \(120\) group transformations are exhaustive, the partition is complete.

**4. Base divisors and arithmetic splitting.** For a basis \(f,g\), the degree of the common homogeneous factor equals the ordinary gcd degree of \(f(X,1),g(X,1)\) plus the shared vanishing order at \([1:0]\). This gives \(3710,70,40\) pencils with respective base-divisor degrees \(0,2,3\). A rational common zero \(P\) is impossible: evaluation of the first derivative at \(P\) is a linear functional on \(W\). It has a rational nonzero kernel member (or is identically zero), which would have a repeated zero at \(P\), contrary to the defining condition. Thus each positive-degree base divisor is a single irreducible closed point of degree two or three. For degree three, every irreducible cubic \(h\) determines the unique pencil \(hH^0(\mathcal O(1))\), yielding \((5^3-5)/3=40\) directly. The \(70\) quadratic-base pencils agree with the quadratic-conic count: for each of ten irreducible quadratic factors \(h\), seven external lines to the discriminant conic in the plane of quadratic forms avoid the point \([h]\).

Every squarefree member factors into irreducible closed-point degrees partitioning four. Trial division by every monic irreducible polynomial of degrees at most four, with the point at infinity included separately, gives the full six-member profile table in `data/census_catalogue.json`. The independent gcd-based approach and the RREF-based irreducible-factor approach agree on every one of the \(14\) profile frequencies. The squarefree-pencil condition also implies at most one completely split member, since two disjoint four-element sets cannot lie in the six-element source \(\mathbf P^1(k)\), and distinct members of a pencil have no common rational root.

## Verification
Run `python code/enumerate_by_pairs.py` and `python code/verify_rref.py` using Python 3 with its standard library only. Compare their console output with `data/reference_output.txt`. The second program writes `verify_reference.generated.json` in the current working directory; compare its parsed JSON with `data/census_catalogue.json`. Both enumerators have been run, and the distribution tables, orbit counts and all fourteen fibre-profile multiplicities match exactly.

The computation is finite and exhaustive: it covers \(781\) projective forms, \(20\,306\) pencils, \(120\) group elements and all six members of each pencil. It does not use random sampling, numerical approximations or inference from bounded examples. The zero-rational-basepoint and cubic-base-subcase claims also have independent mathematical arguments above.

## Relationship to prior work
Asgarli–Ghioca (2022) motivates the problem of linear systems whose every rational member is smooth, proving broad existence results for higher-dimensional hypersurfaces; it does not contain this fixed-field binary-quartic orbit and fibre census. Wall (1998) studies the geometric invariant theory and ramification strata of pencils of binary quartics, including positive-dimensional families and symmetry types; that work supplies the natural objects and geometric comparison, not the exact \(\mathbf F_5\)-rational all-squarefree counts or the \(47\) source-coordinate orbits. The 2022 finite-field classification of pencils of *binary cubics* addresses a different degree and ambient parameter space. These distinctions concern implications of the results, not similarity of titles.

## Limitations
The orbit equivalence is source \(\operatorname{PGL}_2(\mathbf F_5)\), not isomorphism of genus-one curves. No claim is made about all degree-four maps over other finite fields, geometric moduli over an algebraic closure, or the entire degree-six branch discriminant of every pencil. An earlier unindexed finite-field orbit computation may exist; present literature searches do not constitute proof of global publication priority. The source-comparison conclusions are restricted to material actually inspected.

## References
1. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169 (first posted 2022-03-14), published *Bull. Aust. Math. Soc.* 107 (2023), 85–94. DOI: 10.1017/S0004972722000776.
2. C. T. C. Wall, *Pencils of binary quartics*, *Rendiconti del Seminario Matematico della Università di Padova* 99 (1998), 197–217. Available from https://www.numdam.org/article/RSMUP_1998__99__197_0.pdf.
3. *On pencils of cubics on the projective line over finite fields of characteristic greater than three*, *Finite Fields and Their Applications* 78 (2022), 101960. DOI: 10.1016/j.ffa.2021.101960.
