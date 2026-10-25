# Scientific review

## Correctness: PASS

The claim has two parts: the global bound \(\alpha(X)\ll X/\log\log X\) and the local-density optimality *only within* independent-Zumkeller-seed coprimality sieving. Both use explicit arguments in RESULT.md. Li's Lemmas 3.1 and 3.2 are reconstructed using residues modulo \(2pw\) and \(2z\operatorname{rad}(z)\), with uniform Linnik thresholds. The published odd Zumkeller-block theorem supplies existence. The block Euler product is squeezed between \(2\) and \(2(1+1/Q)\); the squarefactor Euler product differs from one by \(O(1/P)\). Mertens gives \(Q\asymp P^2\), and Bertrand supplies disjoint consecutive blocks with \(\log z_j\le\exp(D2^j)\). The summable relative errors yield the finite positive product constant. The CRT count *includes* an \(O(Z_r)\) endpoint term and is valid without assuming full periods in \([1,X]\). The depth choice makes both threshold and endpoint errors \(X^{o(1)}\). Odd exceptions are handled separately with a power saving. The divisor-sum/totient identity establishes the method-level limiting obstruction. The finite verifier provides corroborating arithmetic checks but is not used to infer an infinite result.

## Originality: PASS (best-knowledge comparison)

The principal published comparison is Li, arXiv:2610.19574v1: its stated exponent is \(A=\log_2(2\pi^2/(2\pi^2-3))\approx0.2378\), and its displayed proof only uses a uniform local constant \(3/(2\pi^2)\). The new upper bound has exponent \(1\), and the local product has a positive limiting constant; neither conclusion appears in its inspected theorem/proof. Somu--Kukla--Tran, arXiv:2310.14149v2, establish the requisite block property, not the sharper additive exceptional count. The 1974 divisor-subset lemmas establish primitive pseudoperfect structure, not the additive counting claim. Literature searches for equivalent wording, arithmetic reformulations, stronger bounds, and exact tables did not identify a covering result. The new argument is a refinement of Li's construction, so its dependence and the risk of an unstated consequence of general sieve principles are explicitly acknowledged; absence of a search hit is not a proof of global novelty.

## Mathematical value: PASS

The new theorem improves a recently established quantitative zero-density estimate in an active additive representation problem from exponent approximately \(0.238\) to \(1\), a change in asymptotic decay order rather than a numerical constant. The summably sharp local coprimality law identifies the exact asymptotic defect of the basic independent-block sieve, explains why the earlier constant loses density exponent, and quantifies the finite CRT error that is required for a genuinely uniform counting statement. These provide mathematical use beyond a single computed instance. The result explicitly does not claim universal optimality of exponent \(1\).

## Closest literature and limitations

The proof depends on Li (2026) for the general least-prime representation framework and Somu--Kukla--Tran (2023), ultimately Benkoski--Erdős (1974), for existence of odd prime-block Zumkeller seeds. The asymptotic bound lacks an explicit starting threshold; the seed product constant depends on the first admissible block. A stronger implicit literature result remains a residual originality risk. The verification is finite; no external independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
