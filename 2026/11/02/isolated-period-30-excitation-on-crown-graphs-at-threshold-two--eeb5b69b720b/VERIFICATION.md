---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The finite saturation lemma reduces any labelled crown graph to nine populations clipped at three; each occupied original pair type is tracked independently. The source `verify.cpp` exhaustively traverses every nonempty saturated vector and the tagged microscopic orbit, with exact integer transitions and no sampling. Its output confirms 262143 nonempty population vectors, maximum preperiod nine, all and only the periods 1, 3, 4, 6, 10, 12, and 30, and exactly two recurrent period-30 population vectors, each having eight distinct pair types of multiplicity one.

The pair-type vectors corresponding to period 30 are (1,1,1,1,1,1,1,0,1) and (1,1,1,1,1,0,1,1,1) in order (00,01,02,10,11,12,20,21,22). They each contribute 8! labelled states on the eight-pair graph; hence the number of primitive period-30 cycles is 2*8!/30 = 2688. The program explicitly validates every period-30 capped vector is an all-zero-or-one occupancy vector with exactly eight occupied classes, ruling out such periodic behaviour at any other size.

`direct_check.py` independently updates every vertex instead of using capped populations. It exhausts the 3^(2n) labelled configurations for n = 1 through 5 and checks explicit primitive-period-30 witnesses for n = 8 and a sharp preperiod-nine witness for n = 9. It does not replace the all-size exhaustive capped certificate. All standard compilation, executable output, and actual source paths are included in this self-contained package. Historical novelty remains qualified; no external or independent audit was performed.
