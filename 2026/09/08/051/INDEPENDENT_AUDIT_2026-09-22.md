# Independent audit — Walsh census of Boolean functions

**Review date (UTC):** 2026-09-24  
**Source path:** `2026/09/08/051`  
**Audited source tree:** `94db5efb91f5e6caeb09d4ef2bdbc1a365fcccb9`  
**Review type:** separate AI independent audit.

## Claim audited

The record gives the complete joint nonlinearity/resiliency distribution of all 65,536 Boolean functions in four variables and of the 256 cyclic rotation-symmetric Boolean functions in five variables, together with explicit Walsh-spectrum witnesses and the classical consequence `rho(RM(1,4))=6`.

## Correctness — PASS

I independently enumerated every four-variable truth table and recomputed its Walsh spectrum by an integer fast Walsh-Hadamard transform, asserting Parseval on every function. The resulting joint cells exactly match the record: `(0,-1):2,(0,0):8,(0,1):12,(0,2):8,(0,3):2,(1,-1):512,(2,-1):1920,(2,0):1920,(3,-1):17920,(4,-1):17080,(4,0):10720,(4,1):200,(5,-1):14336,(6,-1):896`, totaling 65,536. The nonlinearity marginal is `32,512,3840,17920,28000,14336,896` for values 0 through 6.

Using the eight listed cyclic orbits on 32 inputs, I independently enumerated all 256 five-variable rotation-symmetric functions. The joint table again matches exactly: `(0,-1):2,(0,4):2,(1,-1):8,(2,-1):2,(2,0):2,(5,-1):24,(6,-1):48,(7,-1):24,(10,-1):18,(10,0):18,(11,-1):72,(12,-1):18,(12,0):10,(12,1):8`. Mask 30 reconstructs truth table 2165774206 and the exact spectrum printed in the record, with nonlinearity 12 and resiliency 0. Parseval also gives the standard upper bound 6 at n=4, attained by the bent functions.

## Originality — PASS relative to checked literature

Several marginals are classical and are properly identified as such. The 2008 Stănică–Maitra paper `Rotation symmetric Boolean functions—Count and cryptographic properties` already completely searches the five-variable rotation-symmetric class and, in §3.2.1, explicitly reports the eight `(5,1,3,12)` functions; thus that extremal cell is prior art. Likewise the 896 four-variable bent count and the n=4 nonlinearity marginal are long known. However, I did not find the record's full 15-cell nonlinearity-by-resiliency table for either scope in the checked sources. The surviving originality is therefore only the complete joint stratification and replay artifact, not the individual classical extremal counts.

## Scientific value — PASS

The joint tables are small but natural exact benchmark datasets connecting two standard cryptographic invariants. They supply complete ground truth for the last tiny full Boolean-function space and for a literature-standard symmetry slice, useful for validating Walsh/resiliency implementations and for locating all cells rather than only extremizers. This is limited benchmark value, but it remains a concrete reusable invariant after subtracting the classical marginals.

No repair was needed. Full five-variable space and non-cyclic symmetry classes are out of scope.

**Final disposition: PASSED.**
