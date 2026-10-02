# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **passed**.

- Correctness: **PASS.** The excess \(E=\sigma(2^a p^b)-2^{a+1}p^b\) reduces to \(E=M(1+p+\cdots+p^{b-1})-p^b\) with \(M=2^{a+1}-1\). Parity forces \(b\) odd. For \(b=1\), the two possible divisor shapes give exactly the binary-deviation, isolated \(40\), and even-perfect-divisor families. For odd \(b\ge3\), splitting by \(v_p(M)\) eliminates the zero-valuation case, forces \(b=3\) and \(M=p\) in the intermediate case, and rules out the high-valuation case using the exact two-adic valuation of the geometric sum. Thus the four families are exhaustive. The repository's bounded computation is consistent with the proof but is not used as an infinite certificate.
- Originality: **PASS.** The individual sufficient constructions are substantially prior: Firoozbakht--Hasler give the binary-deviation construction, the Mersenne-cube construction, and perfect-divisor mechanisms. The complete 1960 Sachs article defines admirable numbers and lists elementary examples/conjectures but contains no prime-support classification. The surviving contribution is the converse proving that these mechanisms exhaust support \(\{2,p\}\), with odd-prime exponent only \(1\) or \(3\); no earlier converse was located.
- Scientific value: **PASS.** The theorem closes a natural prime-support slice of the admirable-number problem: it turns several previously sufficient Mersenne/perfect-number mechanisms into an exhaustive classification and proves the strong exponent restriction \(b\in\{1,3\}\). This is a complete structural classification rather than a bounded census.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and
`INDEPENDENT_AUDIT_2026-10-01.json`. Earlier same-model scientific evidence
remains separately identified in `AUDIT.json` and is not relabeled as this
independent assessment.
