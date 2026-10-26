# Exact joint squareful local densities and sharp multiplicity thresholds for diagonal quadratic forms

## Finding

For every odd prime \(p\) and every integer \(k\geq1\), consider \(k\) diagonal forms
\[
F_i(X,Y)=a_iX^2+b_iY^2,\qquad a_i,b_i\in\mathbb Z_p^\times.
\]
Equip the primitive part \(U_p=\mathbb Z_p^2\setminus p\mathbb Z_p^2\) with conditional normalized Haar measure. Let \(\delta_p\) be the measure of pairs \((x,y)\in U_p\) satisfying \(v_p(F_i(x,y))\ne1\) simultaneously for every \(i\); \(v_p(0)=+\infty\).

Define \(t_i=-b_i/a_i\in\mathbb Z_p^\times\). Let \(\Lambda\) be the set of distinct nonzero quadratic-residue values among \(t_i\bmod p\), put \(s=|\Lambda|\), and define \(h\) as the number of \(\lambda\in\Lambda\) for which **all** \(t_i\bmod p^2\) with \(t_i\equiv\lambda\pmod p\) coincide. A singleton fiber counts toward \(h\). Then the exact joint squareful local density is
\[
\boxed{\delta_p=1-\frac{2}{p+1}\left(s-\frac{h}{p}\right).}
\]

Put \(q=(p-1)/2\) and \(m=\min(k,q)\). Over all such families of exactly \(k\) forms, the exact *minimum* density is
\[
\boxed{\delta_{p,k}^{\min}=1-\frac{2}{p+1}\left(m-\frac{\max(0,2m-k)}{p}\right).}
\]
It is achieved for every \((p,k)\). All minimizing families are characterized by \(s=m\) and \(h=\max(0,2m-k)\). In particular, for \(k\ge p-1\) the sharp, positive bound is \(\delta_p\ge 2/(p+1)\), with equality precisely when every nonzero square slope is represented and every such slope has two distinct lifts modulo \(p^2\).

## Assumptions and scope

The prime \(p\) is odd. Both coefficients of every form must be units at \(p\), and the domain excludes pairs with both coordinates divisible by \(p\). There is no positivity or global coprimality hypothesis. The local condition forbids valuation exactly one, not all positive valuations. The result is a local, conditional density and a sharp optimization over coefficient choices; it does **not** assert a global counting asymptotic for simultaneous squareful values.

## Proof

**Step 1 (root-line count).** Work modulo \(p^2\), since whether \(v_p(F_i)=1\) is completely determined there. The primitive residue pairs have cardinality \(p^4-p^2\). Since \(a_i\) is a unit, a form is zero modulo \(p\) exactly where \(x^2=t_i y^2\pmod p\). In primitive pairs this is impossible if \(y\equiv0\pmod p\), so \(y\) is a unit. For a nonsquare slope there are no primitive roots. Each quadratic-residue slope \(\lambda\) has two distinct roots \(x/y=\pm r\) in \(\mathbb F_p^\times\), and therefore exactly \(2(p-1)\) primitive root vectors modulo \(p\). Root vectors belonging to different slopes are disjoint.

**Step 2 (a shared-root fiber).** Fix a primitive root vector for \(\lambda\). There are exactly \(p^2\) lifts of it modulo \(p^2\). For a form of slope \(t_i\equiv\lambda\pmod p\), its allowable lifts at this root satisfy \(x^2=t_i y^2\pmod{p^2}\), a single nonempty affine line containing exactly \(p\) of the \(p^2\) lifts. This uses \(2x\not\equiv0\pmod p\). For two forms in the same fiber, the two affine lines agree if and only if their parameters \(t_i\) agree modulo \(p^2\): subtract their congruences and use that \(y\) is a unit. Otherwise the lines are disjoint. Hence the number of accepted lifts is \(p\) if all lifted parameters coincide, and zero if any differ.

**Step 3 (density formula).** For each represented slope, the number of excluded primitive vectors modulo \(p^2\) is \(2(p-1)(p^2-p)\) for a coherent fiber, or \(2(p-1)p^2\) for an incoherent fiber. Dividing their sum by \(p^4-p^2\) yields \(2(p+1)^{-1}(s-h/p)\). Subtract from one to obtain the displayed density. The formula is exact for \(p\)-adic Haar measure because the event is constant on residue classes modulo \(p^2\).

**Step 4 (optimization at fixed form count).** Suppose \(s\) distinct square slopes occur, where \(1\le s\le\min(k,q)\). A fiber can be incoherent only if it has at least two members. Hence at most \(k-s\) of the \(s\) fibers can be incoherent, and
\[
h\ge\max(0,2s-k).
\]
Equality is attainable by placing at least one form in each fiber and using a second, incongruent lift in as many fibers as possible. A square slope always has at least two distinct unit lifts modulo \(p^2\). The excluded-mass objective is therefore bounded above by
\[
G(s)=s-\frac{\max(0,2s-k)}p.
\]
This is strictly increasing in integer \(s\): its slopes are \(1\) before \(2s=k\) and \(1-2/p>0\) afterward (including the crossing). Its maximum is at \(s=m\), with equality precisely when \(s=m\) and \(h=\max(0,2m-k)\). This gives the minimum density and equality classification.

**Step 5 (realization and saturation).** Select any \(m\) distinct nonzero square classes \(\lambda\pmod p\), and for each take the form \(X^2-\lambda Y^2\) (with integer unit lifts of \(\lambda\)). For \(\min(m,k-m)\) selected classes add a form \(X^2-(\lambda+p)Y^2\); any remaining forms repeat existing forms. The required \(s\) and \(h\) result. When \(k\ge 2q=p-1\), every one of the \(q\) square slopes can be made incoherent, giving \(1-2q/(p+1)=2/(p+1)\), and the equality characterization follows.

## Verification

Run the standalone standard-library file `verify.py` using `python verify.py`. It directly enumerates all primitive coordinate pairs modulo \(p^2\) for \(p\in\{3,5,7,11\}\), checks the forbidden valuation-one condition directly, and compares its exact rational frequency with both displayed formulas. It covers random families at \(1\le k\le7\) and explicitly constructed minimizers for every such configuration. The recorded run completed `CERTIFICATE_OK primitive_pair_counts 553 primes 4 k range(1, 8)`. These finite tests are corroboration; Steps 1–5 prove the statements for every allowed \(p,k\).

## Relationship to prior work

Pohl's October 2026 paper [1] establishes an asymptotic for squareful values of a **single** binary quadratic form and develops corresponding local factors. Shute [2] studied a single quadratic-form squareful condition and Campana leading constants. The present statement instead concerns a shared primitive input and an arbitrary family of forms, where collisions of roots **modulo \(p^2\)** change the local density even when all reductions **modulo \(p\)** agree. The exact fixed-\(k\) minimization and its equality structure are additional conclusions, not consequences stated in [1] or [2]. General local sieves and elementary Hensel lifting explain the method, but neither targeted work states the collision-sensitive optimization.

For example, at \(p=5\) the families \((X^2-Y^2,X^2-26Y^2)\) and \((X^2-Y^2,X^2-6Y^2)\) have identical roots modulo \(5\) for their two members, but their respective joint densities are \(11/15\) and \(2/3\), because the square slopes agree modulo \(25\) in the first pair and disagree in the second. This demonstrates why the second residue digit is essential.

## Limitations

The argument excludes \(p=2\), nonunit coefficients, nondiagonal and degenerate reductions, and constraints involving valuations other than exactly one. It is an independent local counting statement, not a proof of simultaneous global asymptotics or any Euler-product convergence assertion. Earlier work on multicomponent Campana divisors or local sieve densities may contain equivalent consequences not identified in the inspected sources; the elementary Hensel argument itself is classical. Independent mathematical review has not been performed.

## References

[1] Sarah Sophie Pohl, *S-squareful values of binary quadratic forms*, arXiv:2610.20316v1, first public 2026-10-14, https://arxiv.org/html/2610.20316v1. Particularly Introduction, §§5, 7.2.4.

[2] Alec Shute, *On the leading constant in the Manin-type conjecture for Campana points*, arXiv:2104.14946v2, https://arxiv.org/pdf/2104.14946. Particularly Introduction and §6.

[3] Valentin Blomer, *Binary quadratic forms with large discriminants and sums of two squareful numbers II*, J. London Math. Soc. 71 (2005), 69–84, doi:10.1112/S0024610704006040 (abstract inspected; its simultaneous representation problem differs).
