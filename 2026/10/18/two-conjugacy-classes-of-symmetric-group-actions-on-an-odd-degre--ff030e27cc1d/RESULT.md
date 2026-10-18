# Two conjugacy classes of \(S_3\) actions on a hyperelliptic family

## Finding
For every integer \(h\ge1\), consider the smooth projective complex curve \(C_h\) birational to \(y^2=t^{12h-5}+t\). Its automorphism group contains precisely \(4h-2\) distinct subgroups isomorphic to \(S_3\). There are exactly two conjugacy classes, each containing \(2h-1\) subgroups. Representatives \(G_\pm\) have quotient genera \(h-1\) and \(h\), respectively. The first action has one order-three branch orbit and four order-two branch orbits; the second has only one order-three branch orbit. The two quotient genera differ despite acting on the same curve.

## Assumptions and scope
Work over \(\mathbb C\). Fix an integer \(h\ge1\), put \(m=12h-6\) and \(k=2h-1\), so \(m=6k\) and \(k\) is odd. Let \(\omega^3=1\) with \(\omega\ne1\). Define automorphisms
\[
r(t,y)=(\omega t,\omega^2y),\quad s_\pm(t,y)=(t^{-1},\pm y/t^{6h-2}).
\]
These formulas define automorphisms of the smooth projective model and satisfy \(r^3=s_\pm^2=1\), \(s_\pm r s_\pm=r^{-1}\). Here "branch orbit" means a single orbit of points with nontrivial stabilizer for the finite covering \(C_h\to C_h/G\). The hyperelliptic genus is \(6h-3\), since the branch polynomial has degree \(12h-5\) and is separable.

## Proof
**1. Full group needed for exhaustive classification.** The hyperelliptic branch set on the \(t\)-line is \(\{0,\infty\}\cup\{t:t^m=-1\}\), of size \(m+2\ge8\). Its reduced automorphism group contains the \(m\)-fold rotation \(t\mapsto\zeta_mt\) and inversion \(t\mapsto t^{-1}\). By classification of finite subgroups of \(\operatorname{PGL}_2(\mathbb C)\), a group with an element of order \(m\ge6\) is cyclic or dihedral; inversion excludes cyclicity. Every rotation in the enlarged dihedral group has the same two fixed points \(0,\infty\), so it is \(t\mapsto\lambda t\). Preserving the nonzero branch set forces \(\lambda^m=1\). Thus the reduced group is exactly dihedral of order \(2m\).

Choose a primitive \(2m\)-th root \(\xi\), put \(\zeta_m=\xi^2\), and let \(\rho(t,y)=(\zeta_mt,\xi y)\) and \(s=s_+\). The full automorphism group has order \(4m\), contains the hyperelliptic involution \(\rho^m\), and has presentation
\[
\rho^{2m}=s^2=1,\qquad s\rho s=\rho^{m-1}.
\]
Indeed the lift \(\rho\) has order \(2m\), inversion lifts to \(s\), and these account for both lifts of every reduced automorphism. The conjugation formula follows on both coordinates (the factor \(\zeta_m^{m/2}=-1\) is essential).

**2. Subgroups and conjugacy.** Write the full group elements as \(\rho^a\) or \(\rho^a s\), with \(a\) modulo \(2m\). The unique subgroup of order three is \(A=\langle\rho^{2m/3}\rangle\). No element in the other coset has order three because \((\rho^a s)^2=\rho^{ma}\). The elements of order two outside the cyclic subgroup are precisely \(\rho^{2j}s\). Every \(S_3\)-subgroup must contain \(A\) and one of these reflections; conversely each \(H_j=\langle A,\rho^{2j}s\rangle\) is \(S_3\). The equivalence \(H_j=H_{j+m/3}\) and no others gives \(m/3=2k=4h-2\) distinct subgroups. Conjugation by \(\rho\) changes \(j\) by \(1-m/2\) modulo \(m/3=2k\). Since \(m/2=3k\) is odd, this increment is even and has greatest common divisor \(2\) with \(2k\), hence there are exactly two conjugacy classes, distinguished by parity of \(j\), each of size \(k\). They are represented by \(s_+=s\) and \(s_-=\rho^m s\) (the latter has odd \(j=m/2\)).

**3. Branch data.** The nonidentity elements of \(A\) fix precisely the two points over \(t=0\) and \(t=\infty\), interchanged by \(s_\pm\); these form one branch orbit of inertia \(3\). For \(s_+\), the fixed parameters are \(t=\pm1\) and each carries two distinct fixed points because \(t^{6h-2}=1\) there. Thus \(s_+\) fixes four points. Its two conjugate transpositions also fix four points each, with disjoint fixed sets (an overlap would require a point fixed by \(A\), which lies over \(0,\infty\)). They produce \(12\) points, i.e. four branch orbits of size three and inertia \(2\). In contrast, \(s_-\) fixes no point since at \(t=\pm1\) its action negates the nonzero \(y\)-coordinate; hence its transpositions contribute no branch orbits. Riemann–Hurwitz reads
\[
2(6h-3)-2=6(2g_- -2)+4=6(2g_+ -2)+4+4\cdot3,
\]
so \(g_-=h\) and \(g_+=h-1\).

**4. Explicit quotients (known involution-quotient framework).** The order-three invariants \(x=t^3\), \(v=ty\) satisfy \(v^2=x^{4h-1}+x\). The involutions \(s_\pm\) induce \((x,v)\mapsto(x^{-1},\pm v/x^{2h})\). Put \(u=x+x^{-1}\) and \(b=v/x^h\). Then \(b^2=x^{2h-1}+x^{-(2h-1)}=P_{2h-1}(u)\), with recurrence \(P_0=2\), \(P_1=u\), \(P_{n+1}=uP_n-P_{n-1}\). For plus sign, \(b\) is invariant, giving \(b^2=P_{2h-1}(u)\). For minus sign, \(b(x-x^{-1})\) is invariant, giving \(b^2=(u^2-4)P_{2h-1}(u)\). In either case the invariant field has index two in \(\mathbb C(x,v)\). The polynomial \(P_{2h-1}\) is squarefree and does not vanish at \(u=\pm2\), so the displayed hyperelliptic genera agree with Riemann–Hurwitz.

## Verification
The attached `check_s3_two_actions.py` enumerates the indicated finite groups and conjugacy classes, verifies stabilizer-count genus identities, and checks the Dickson-polynomial equations for \(1\le h\le15\). It prints `TWO_S3_ACTIONS_GROUP_CHECK_OK` when successful. The uniform conclusions follow from the arguments for arbitrary \(h\), not extrapolation from finite calculations.

## Relationship to prior work
Pan (2026) constructs the \(G_-\) action, proves its genus-\(h\) quotient and single order-three ramification orbit in connection with the Polishchuk–Van den Bergh conjecture. Novoselov (2019/2020), building on older work, provides the general dihedral-automorphism and Dickson-polynomial involution-quotient equations: the two equations above are therefore **not claimed as new**. The present claim is the exhaustive two-conjugacy-class classification of \(S_3\) subgroups on Pan's precise family, with the distinct branch data of the two actions. The full hyperelliptic automorphism presentation is likewise only a tool, not an independently novel result.

## Limitations
The action-classification is over the algebraically closed complex field; it does not classify field-of-definition forms, all possible finite subgroups, derived-category decompositions, or equivalences of quotient curves beyond those displayed. General dihedral automorphism theory and the two Dickson quotient models significantly predate this result. A fuller historical treatment of \(S_3\) subgroups might contain an equivalent classification; this residual originality risk remains.

## References
1. Shengyong Pan, *Counterexamples to the Polishchuk--Van den Bergh conjecture on curves*, arXiv:2610.10147v1 (first publicly submitted 2026-10-07), Section 3.
2. S. A. Novoselov, *Counting points on hyperelliptic curves of type \(y^2=x^{2g+1}+ax^{g+1}+bx\)*, arXiv:1902.05992 (2019); *Finite Fields and Their Applications* 68 (2020), 101757, Section 2.
