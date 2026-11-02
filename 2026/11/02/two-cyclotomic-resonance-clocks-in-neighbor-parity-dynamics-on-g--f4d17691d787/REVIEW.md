# Scientific review

## Correctness — PASS

The graph's synchronous binary adjacency operator has the two-by-two Laurent symbol \(B=\begin{pmatrix}y&1\\1&y^2\end{pmatrix}\) with \(y=z+z^{-1}\), and determinant \(z^{-3}\Phi_3\Phi_5\). The two local resonances have different zero-Jordan blocks: two size-\(2e\) blocks at \(3\mid n\), and four size-\(e\) blocks at \(5\mid n\). The proof derives the first-entry counts, then separately obtains fixed points and all-time returns by Smith normal form. Exact independent matrix/polynomial comparisons corroborate the algebraic steps but are not claimed as an infinite proof. The full proof and replay commands are in `RESULT.md` and `VERIFICATION.md`.

## Originality — PASS, with residual risk

Gera–Stănică (2011), *The spectrum of generalized Petersen graphs*, Theorem 2.4 and Section 3, provide the two-circulant adjacency block and a characteristic-zero eigenvalue equation for the same family. Those are credited, but they do not state characteristic-two repeated-root Jordan chains or exact entry-time shells. Zaidenberg (2006, 2009) develops the finite-field convolution/Fourier framework; its inspected periodic Fourier statements concern periods prime to the characteristic, and do not directly give the even-\(n\) repeated-root results. Relevant primary material was actually read, not inferred from its title. Searches of equivalent formulations, stronger coverage and exact tables identified no complete statement of this claim, but cannot exclude unindexed prior equivalents.

The close alternative cubic family \(C_n\square K_2\) has a different characteristic-two determinant and lacks the separate five-resonance. Claims about that family therefore do not imply the present graph's new arithmetic dichotomy.

## Mathematical value — PASS

The result determines the entire distribution of entry into the recurrent state set for all sizes of a standard infinite graph family. The distinct divisibility obstructions \(3\mid n\) and \(5\mid n\), their different Jordan lengths, and their exact cumulative state counts are qualitative structure, not a one-off table or a mere rephrasing of invertibility. The exact return-time procedure additionally makes the period census computable for arbitrary chosen parameters.

## Limitations and sources

The theorem is restricted to \(GP(n,2)\), \(n\ge5\), synchronous open-neighborhood binary parity. The return-time formula is an algorithmic polynomial-gcd expression; no elementary closed formula for maximum primitive period at every size is claimed. Full primary reading covered Gera–Stănică (2011) and relevant specified portions of Zaidenberg (2006, 2009). A hidden historical characteristic-two equivalent remains possible. No independent scientific validation is claimed.

Self-review: passed. Independent audit: not yet performed.
