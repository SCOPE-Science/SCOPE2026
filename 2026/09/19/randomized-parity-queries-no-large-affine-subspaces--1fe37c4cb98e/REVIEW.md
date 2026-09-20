# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Three points were checked separately.

First, the Wang-Wu total function is genuinely an XOR function on the parties' complete inputs. Their Definition 3.8 uses only \(z=x\oplus y\) and the addressed certificate \(c_h=u_h\oplus v_h\). Hence there is a total one-input function \(\phi_N\) with \(F(a,b)=\phi_N(a\oplus b)\).

Second, the randomized communication upper bound descends to a parity-query upper bound for this particular protocol. The address stage samples \(kq\) coordinates of \(z\), which are singleton parity queries. The certificate test uses four linear queries over \(\mathbb F_{2^{4k}}\). Under any fixed binary basis, each field-valued linear answer consists of \(4k\) binary linear functionals, so four such answers require \(16k\) parity queries. The central algorithm then applies the same acceptance rule and inherits the same error analysis. Thus \(R^\oplus(\phi_N)=O(k\log k)=O(\log N\log\log N)\).

Third, the affine-subspace lower bound is an exact XOR reduction. If \(C=a+H\) is monochromatic for \(\phi_N\) and has codimension \(r\), then \(H\times(a+H)\) is monochromatic for \(F\) and has density \(2^{-2r}\). Wang and Wu's Theorem 5.1 gives rectangle density at most \(2^{-m/(8k)}\), hence \(r\ge m/(16k)=N^{\Omega(1)}\). This also lower-bounds deterministic parity-query depth because each deterministic leaf is a monochromatic affine subspace of codimension at most the depth.

Potential failure modes were checked: the address is adaptive but parity decision trees permit adaptive queries; the field queries are not single binary parities but expand into exactly \(4k\) binary parities per field element; and the \(\operatorname{Ind}(z)=0\) branch remains valid because the source soundness analysis applies to every selected certificate.

## Originality

**PASS, to the best of our knowledge.** Gavinsky's 2025 paper explicitly states Question 14: whether every Boolean function with an efficient randomized parity-query protocol is constant on a large affine subspace. The same paper explains that an efficient parity-query protocol lifts to a restricted XOR communication protocol and that a monochromatic affine subspace yields a monochromatic rectangle.

The full Wang-Wu report was inspected at the theorem, construction, protocol, and rectangle-bound statements. It proves an \(O(\log N\log\log N)\) randomized communication protocol and a \(2^{-N^{\Omega(1)}}\) maximum monochromatic-rectangle density for a total function. The inspected version does not formulate a parity-query result, an XOR-quotient theorem, an affine-subspace consequence, or a resolution of Gavinsky's Question 14. Its construction nevertheless visibly depends only on \((x\oplus y,u\oplus v)\), and its fully linear PCP is precisely what makes the descent possible.

Targeted literature searches used the exact source identifier and title together with "parity query", "parity decision tree", "affine subspace", "XOR function", and Gavinsky's "Question 14". Searches also included synonymous formulations such as randomized parity-query functions without large monochromatic affine subspaces. No prior statement of this consequence was found. Hatami-Hosseini-Lovett's deterministic XOR-function simulation theorem was checked as nearby prior art; it does not supply the randomized implication used here and identifies the randomized direction as a separate issue.

The current SCOPE archive was searched by the source identifier, parity-query terminology, affine-subspace terminology, and recent records; no overlapping finding was found. Because the Wang-Wu report is very recent and the new deduction is short once its XOR structure is noticed, near-simultaneous observation and folklore risk are material. No inaccessible source was identified that gives concrete evidence of prior coverage.

## Value

**PASS.** The statement resolves an explicit open structural question in the strongest qualitative direction: randomized parity queries of polylogarithmic complexity need not leave even a monochromatic affine subspace of polylogarithmic codimension. Quantitatively, every such affine subspace has codimension at least \(m/(16k)=N^{\Omega(1)}\), while the randomized parity-query complexity is \(O(\log N\log\log N)\).

The result also cleanly separates the deterministic and randomized parity-query models on a total Boolean function, with \(D^\oplus(\phi_N)=N^{\Omega(1)}\) versus \(R^\oplus(\phi_N)=O(\log N\log\log N)\). The contribution is a consequence of a new communication construction, not a new general simulation theorem.

## Limitations

The argument is specific to the Wang-Wu protocol's sampled XOR coordinates and fully linear PCP queries. It does not prove that every efficient randomized protocol for an XOR function descends to an efficient randomized parity decision tree. The exponent hidden in \(N^{\Omega(1)}\) is not optimized here, and all priority claims remain subject to the very recent literature around the motivating construction.
