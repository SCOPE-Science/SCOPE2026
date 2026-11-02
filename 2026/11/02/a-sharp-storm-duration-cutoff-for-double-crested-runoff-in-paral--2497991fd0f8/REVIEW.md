# Scientific review of the finite-storm hydrograph modality theorem

## Correctness — PASS

The two-Erlang kernel is the standard impulse response of two equal-rate serial linear reservoirs. A single uniform pulse produces an explicit difference of two kernel values in the derivative; all post-pulse zeros lie strictly between the two positive single-kernel modes. A positive odds ratio controls every derivative sign. Its logarithmic derivative has at most two zeros with an exact discriminant; the strict convexity proof for \(\(z/(e^z-1)\)\) yields exactly one duration cutoff when \(r>3+2\sqrt2\). Boundary cases are included. Rational signs at four explicit times prove two strict crests in the example, while one inequality excludes multiple crests after doubling storm duration. The extracted reproducibility script passed 1797 assertions. The analytical proof, not numerical tests, establishes general quantifiers.

## Originality — PASS within inspected evidence

Došlá's 2009 Theorem 2 gives a broad pre-existing modality criterion for two-unimodal-density mixtures, and Proposition 6 already contains the instantaneous common-shape gamma-mixture threshold. The novelty claim excludes those general and instantaneous results and instead establishes the **unique positive rectangular-storm duration cutoff** and **complete admissible mixing interval** for a paired Nash-2 pathway model. Hydrologic parallel-cascade and convolution literature supplies the model but did not, in the material inspected, establish this finite-duration classification. The 1978 source was accessible only as a publisher abstract; despite that access limitation, its identified modeling scope is not direct evidence of the precise finite-storm theorem, and historical priority remains provisional. Related published mathematical research records were searched by aliases and implications, rather than by title alone.

## Value — PASS

One storm rather than two pulses can generate two peaks, and changing only its duration can erase all second crests at an exact, universal network-dependent threshold. This separates structural routing-induced multi-peaking from multiple rainfall events and supplies a precise identifiable parameter regime. A complete, sharp, interpretable boundary for a natural routing model is useful for conceptual model design and diagnostic hydrograph analysis, without implying empirical validity for any particular catchment.

## Limitations and closest literature

The instantaneously mixed-gamma result (Došlá 2009), gamma-mixture inflection study (Ahmed, Goria and Hussein 2008), the linear unit-hydrograph convolution (Bárdossy, Mascellani and Franchini 2006), and early parallel-cascade watershed architecture (Diskin, Oben-Nyarko and Ince 1978) are acknowledged. The latter original text was not available in full. Nonlinear routing, nonrectangular rain, delay, different cascade orders, and empirical inference are unproved. Independent historical-priority assessment is not complete.

Self-review: passed. Independent audit: not yet performed.
