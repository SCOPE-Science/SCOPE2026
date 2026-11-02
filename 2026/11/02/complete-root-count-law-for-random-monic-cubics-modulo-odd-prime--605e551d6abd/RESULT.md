# Complete root-count law for random monic cubics modulo odd prime cubes

## Finding

For every odd prime \(p\), independently choose \(a,b,c\) uniformly from the residue ring \(\mathbb Z/p^3\mathbb Z\), put \(f(X)=X^3+aX^2+bX+c\), and let \(R_p(f)\) be the number of residues \(x\pmod{p^3}\) satisfying \(f(x)\equiv0\pmod{p^3}\). The exact probability-generating function \(\mathbb E[z^{R_p}]\) is

\[
\boxed{\mathcal G_p(z)=\frac{1}{p^3}\left[\frac{p^3-p}{3}+\frac{p^2(p-1)}2z+\binom p3 z^3+p(p-1)z\mathcal Q_p(z)+p\mathcal T_p(z)\right],}
\]
where
\[
\mathcal Q_p(z)=\frac{2p^2-p-1}{2p^2}+\frac{z^p}{p^2}+\frac{p-1}{2p^2}z^{2p},
\]
and
\[
\mathcal T_p(z)=1-\frac{p-1}{p^2}-\frac1{p^3}+\frac{p-1}{p^2}z^p+\frac{z^{p^2}}{p^3}.
\]

In particular, the possible root counts are precisely \(0,1,3,p,p+1,2p+1,p^2\) (colliding values are combined when \(p=3\)). The largest count \(p^2\) occurs with exact probability \(p^{-5}\). The fourth moment is
\[
\boxed{\mathbb E[R_p^4]=p^3+8p^2+2p+4-\frac{42}{p}+\frac{28}{p^2}.}
\]

## Assumptions and scope

The parameter \(p\) is any odd rational prime. The probability space consists of the \(p^9\) monic cubics over \(\mathbb Z/p^3\mathbb Z\), each given equal weight; roots are distinct *residue classes modulo \(p^3\)*, not necessarily roots in the \(p\)-adic integers. In particular, a multiple modular root need not persist to arbitrary precision. No assertion for \(p=2\) is included. The theorem is exact for every odd prime, without an asymptotic or large-prime assumption.

## Proof

**1. Reduction types.** Every monic cubic modulo \(p\) lies in exactly one of the following mutually exclusive cases. The counts of reductions, and the number of simple roots (when applicable), are

| Reduction type | Number of reductions | Simple roots |
| --- | ---: | ---: |
| Irreducible cubic | \((p^3-p)/3\) | 0 |
| One linear factor and an irreducible quadratic | \(p(p^2-p)/2\) | 1 |
| Three distinct linear factors | \(\binom p3\) | 3 |
| One double and one distinct simple linear factor | \(p(p-1)\) | 1 |
| One triple linear factor | \(p\) | 0 |

The entries follow from the standard counts of monic irreducible quadratics and cubics over \(\mathbb F_p\), and from choosing distinct linear roots. Their sum is \(p^3\). Each reduction has exactly \(p^6\) equally likely coefficient lifts. Simple roots lift uniquely to roots modulo \(p^3\), by Hensel's lemma; irreducible factors of degree above one have no residue roots.

**2. The double-plus-simple case.** Fix a reduction \((X-r)^2(X-s)\) with \(r\ne s\) in \(\mathbb F_p\). Hensel factorization gives a unique factorization of every monic lift as \((X-u)q(X)\), where \(u\equiv s\pmod p\) and the monic quadratic \(q\) reduces to \((X-r)^2\). This is a bijection on coefficient lifts, so \(q\) is uniform in its residue class. The simple factor contributes exactly one root; all other roots are precisely those of \(q\) near \(r\).

Write \(q(X)=X^2+vX+w\). Because \(2\) and \(4\) are units modulo \(p^3\), completing the square identifies its roots bijectively with solutions of \(Y^2\equiv\Delta\pmod{p^3}\), with \(\Delta=v^2-4w\). Since \(w\mapsto\Delta\) is an affine bijection and \(q\bmod p\) is a square, \(\Delta\) is uniform over the multiples of \(p\) modulo \(p^3\).

If \(v_p(\Delta)=1\), or \(v_p(\Delta)=2\) with nonsquare unit part, there are no roots. If \(v_p(\Delta)=2\) and its unit part is a square, there are \(2p\) roots. If \(\Delta\equiv0\pmod{p^3}\), there are \(p\) roots. Their respective probabilities of the two nonzero counts are \((p-1)/(2p^2)\) and \(1/p^2\); the remaining probability is \((2p^2-p-1)/(2p^2)\). This gives \(z\mathcal Q_p(z)\).

**3. The triple case.** Fix a reduction \((X-r)^3\), take any integer representative \(r\), and translate \(X=r+Y\). Every lift is uniquely \(f(r+Y)=Y^3+pA Y^2+pB Y+pC\), with \(A,B,C\) independent and uniform modulo \(p^2\). A root must satisfy \(Y=pv\). Modulo \(p^3\),
\[
f(r+pv)\equiv pC+p^2Bv\pmod{p^3}.
\]
Write \(C=C_0+pC_1\) and \(B=B_0+pB_1\) modulo \(p^2\). The root criterion is \(C_0=0\) and \(C_1+B_0v\equiv0\pmod p\). If \(B_0\ne0\), exactly one residue \(v\pmod p\) works, with \(p\) free second digits, yielding \(p\) roots with probability \((p-1)/p^2\). If \(B_0=0\) and \(C_1=0\), all \(p^2\) values \(v\pmod{p^2}\) work, with probability \(1/p^3\). Otherwise there are no roots. This gives \(\mathcal T_p(z)\).

**4. Assemble.** The reduction counts in step 1 weight the root-count laws in steps 2 and 3. Dividing their sum by the total \(p^3\) reductions gives precisely \(\mathcal G_p(z)\). The coefficient of \(z^{p^2}\) is \((p/p^3)(1/p^3)=p^{-5}\); no other reduction type can contribute more than \(2p+1<p^2\) roots for odd \(p\). All displayed coefficients are positive for odd primes (with the two \(z^3\) contributions added at \(p=3\)). Direct expansion of the finite generating function yields the fourth-moment formula. It also yields the consistency identities \(\mathbb E[R_p]=1\), \(\mathrm{Var}(R_p)=3(1-p^{-1})\), and \(\mathbb E[R_p^3]=5p+5-17/p+8/p^2\). This completes the proof.

## Verification

The included standalone C++17 program `verify.cpp` exhaustively enumerates all \(3^9=19683\) and \(5^9=1953125\) monic cubics modulo \(3^3\) and \(5^3\), counts solutions by direct substitution, and checks every histogram count against the theorem. It uses only exact integer arithmetic. Command: `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify`. Output expected and observed:

```
VERIFY_OK p=3 0:7452 1:9963 3:1215 4:486 7:486 9:81 total=19683
VERIFY_OK p=5 0:690000 1:1056250 3:156250 5:12500 6:12500 11:25000 25:625 total=1953125
```

This exhaustive computation is only for the two specified primes; the result for all odd primes is proved in the preceding reduction-type argument.

## Relationship to prior work

Nir (2026) studies deterministic integer-root finding and develops a weighted tree for lifting repeated roots; that paper motivates examining the exact statistical branching of singular roots at low precision, but its main results are algorithmic complexity bounds, not the distribution of cubic root counts over a finite prime-cube ring. Jain (2024) computes expected numbers of zeros over general finite rings and distributions under function-completeness assumptions over finite *fields*; it does not state the present low-degree finite-ring distribution. Bhargava, Cremona, Fisher and Gajović (2022) determine distributions of actual roots in \(\mathbb Q_p\); Caruso (2022) studies \(p\)-adic roots and correlations. These concern persistent \(p\)-adic roots, not all temporary solutions modulo \(p^3\). For example, \(X^3\) has \(p^2\) roots modulo \(p^3\) but only one root in \(\mathbb Q_p\), so their root-count laws do not imply this law by direct identification.

The general Hensel and finite-field factorization ingredients are classical and are not claimed new. The contribution assessed here is the evaluated full seven-level law and its sharp high-root-count probability for the natural low-degree monic-cubic ensemble.

## Limitations

The formula does not include \(p=2\), nonmonic cubics, higher precision or higher degree. The proof is mathematical rather than an independent formal certification. Novelty was compared against the relevant accessible literature but a different previously published equivalent finite-ring enumeration remains a possibility; this does not establish priority over an exhaustive mathematical bibliography. A separate independent review has not been performed.

## References

1. Itamar Nir, *Faster Deterministic Integer Root Finding for Integer Polynomials*, arXiv:2608.00668 (first version, 2026-08-01), https://arxiv.org/abs/2608.00668 . Sections 1 and 5.
2. Ritik Jain, *The number of solutions of a random system of polynomials over a finite field*, arXiv:2409.06866 (2024), https://arxiv.org/abs/2409.06866 . Theorems 1.4 and 1.5, Sections 3 and 4.
3. Manjul Bhargava, John Cremona, Tom Fisher and Stevan Gajović, *The density of polynomials of degree n over \(\mathbb Z_p\) having exactly r roots in \(\mathbb Q_p\)*, Proceedings of the London Mathematical Society 124 (2022), 713–736, https://doi.org/10.1112/plms.12438 . Sections 1 and 2.
4. Xavier Caruso, *Where are the zeroes of a random p-adic polynomial?*, Forum of Mathematics, Sigma 10 (2022), e55, https://doi.org/10.1017/fms.2022.27 .
